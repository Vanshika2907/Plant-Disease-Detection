import os
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from collections import Counter

import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from torchvision import transforms
from PIL import Image


# --------------------------------------------------
# PROJECT PATHS: supports Mac and Kaggle
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BIO_EL_ROOT = PROJECT_ROOT.parent

# Allow the dataset location to be overridden in cloud environments.
# Local project: use the normal project location.
# Kaggle: set PLANT_DATA_ROOT to the mounted dataset location.
ENV_DATA_ROOT = os.environ.get("PLANT_DATA_ROOT")

if ENV_DATA_ROOT:
    DATA_ROOT = Path(ENV_DATA_ROOT)
elif (PROJECT_ROOT / "dataset_cleaning").exists():
    DATA_ROOT = PROJECT_ROOT
else:
    DATA_ROOT = BIO_EL_ROOT

MANIFEST_PATH = DATA_ROOT / "dataset_cleaning" / "final_split_manifest.csv"

IMG_SIZE = 224

EXPECTED_SPLITS = {
    "train": 60027,
    "validation": 13693,
    "test": 12806
}


# --------------------------------------------------
# DATASET
# --------------------------------------------------

class ExpandedPlantDataset(Dataset):

    def __init__(self, dataframe, class_to_idx, transform=None):
        self.dataframe = dataframe.reset_index(drop=True)
        self.class_to_idx = class_to_idx
        self.transform = transform

        self.zip_paths = {}
        self.zip_handles = {}

    def __len__(self):
        return len(self.dataframe)

    def _find_zip(self, zip_relative_path):

        if zip_relative_path in self.zip_paths:
            return self.zip_paths[zip_relative_path]

        # First try the exact path inside the cloud package.
        candidates = [
            DATA_ROOT / zip_relative_path,
            BIO_EL_ROOT / zip_relative_path
        ]

        for candidate in candidates:
            if candidate.is_file():
                self.zip_paths[zip_relative_path] = candidate
                return candidate

        # Fallback for the original Mac ZIP-based manifest.
        zip_name = Path(zip_relative_path).name
        matches = list(BIO_EL_ROOT.rglob(zip_name))

        if not matches:
            raise FileNotFoundError(
                f"Could not find ZIP archive: {zip_relative_path}"
            )

        self.zip_paths[zip_relative_path] = matches[0]
        return matches[0]

    def _load_image(self, location):

        location = str(location)

        # ------------------------------------------
        # ZIP-based image
        # ------------------------------------------

        if ".zip/" in location:

            zip_relative_path, internal_path = location.split(
                ".zip/", 1
            )

            zip_relative_path += ".zip"

            if zip_relative_path not in self.zip_handles:

                zip_path = self._find_zip(zip_relative_path)

                self.zip_handles[zip_relative_path] = ZipFile(
                    zip_path, "r"
                )

            image_bytes = self.zip_handles[
                zip_relative_path
            ].read(internal_path)

            image = Image.open(
                BytesIO(image_bytes)
            ).convert("RGB")

        # ------------------------------------------
        # Ordinary image file
        # ------------------------------------------

        else:

            image_path = Path(location)

            if not image_path.is_absolute():
                image_path = DATA_ROOT / image_path

            if not image_path.exists():
                raise FileNotFoundError(
                    f"Image not found: {image_path}"
                )

            image = Image.open(image_path).convert("RGB")

        return image

    def __getitem__(self, index):

        row = self.dataframe.iloc[index]

        image = self._load_image(row["location"])
        label = self.class_to_idx[row["class"]]

        if self.transform:
            image = self.transform(image)

        return image, label

    def close(self):
        for archive in self.zip_handles.values():
            archive.close()

        self.zip_handles.clear()


# --------------------------------------------------
# DATALOADER CREATION
# --------------------------------------------------

def get_expanded_dataloaders(
    batch_size=32,
    num_workers=0
):

    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"Manifest not found: {MANIFEST_PATH}"
        )

    df = pd.read_csv(MANIFEST_PATH)

    required_columns = {
        "class",
        "location",
        "final_split"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Manifest is missing columns: {missing}"
        )

    df = df.dropna(
        subset=["class", "location", "final_split"]
    )

    # Validate the expected dataset size.
    if len(df) != 86526:
        raise ValueError(
            f"Expected 86,526 records, found {len(df)}"
        )

    # Alphabetical class mapping, unchanged.
    class_names = sorted(
        df["class"].unique().tolist()
    )

    class_to_idx = {
        class_name: index
        for index, class_name in enumerate(class_names)
    }

    if len(class_names) != 68:
        raise ValueError(
            f"Expected 68 classes, found {len(class_names)}"
        )

    # Separate the original splits.
    train_df = df[
        df["final_split"] == "train"
    ].copy()

    val_df = df[
        df["final_split"] == "validation"
    ].copy()

    test_df = df[
        df["final_split"] == "test"
    ].copy()

    actual_splits = {
        "train": len(train_df),
        "validation": len(val_df),
        "test": len(test_df)
    }

    if actual_splits != EXPECTED_SPLITS:
        raise ValueError(
            f"Split mismatch. Expected {EXPECTED_SPLITS}, "
            f"found {actual_splits}"
        )

    # ------------------------------------------
    # Image transformations
    # ------------------------------------------

    train_transform = transforms.Compose([

        transforms.RandomResizedCrop(
            IMG_SIZE,
            scale=(0.8, 1.0)
        ),

        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(20),

        transforms.ColorJitter(
            brightness=0.15,
            contrast=0.15,
            saturation=0.15
        ),

        transforms.ToTensor(),

        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    evaluation_transform = transforms.Compose([

        transforms.Resize(256),
        transforms.CenterCrop(IMG_SIZE),
        transforms.ToTensor(),

        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # ------------------------------------------
    # Dataset objects
    # ------------------------------------------

    train_dataset = ExpandedPlantDataset(
        train_df,
        class_to_idx,
        train_transform
    )

    val_dataset = ExpandedPlantDataset(
        val_df,
        class_to_idx,
        evaluation_transform
    )

    test_dataset = ExpandedPlantDataset(
        test_df,
        class_to_idx,
        evaluation_transform
    )

    # ------------------------------------------
    # Weighted sampling for training only
    # ------------------------------------------

    train_labels = [
        class_to_idx[name]
        for name in train_df["class"]
    ]

    class_counts = Counter(train_labels)

    sample_weights = [
        1.0 / class_counts[label]
        for label in train_labels
    ]

    sampler = WeightedRandomSampler(
        weights=sample_weights,
        num_samples=len(sample_weights),
        replacement=True
    )

    # ZIP handles are kept inside each dataset object.
    # Start with num_workers=0 for safe ZIP reading.

    train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    sampler=sampler,
    num_workers=num_workers,
    pin_memory=torch.cuda.is_available(),
    persistent_workers=(num_workers > 0),
    prefetch_factor=2 if num_workers > 0 else None
    )

    val_loader = DataLoader(
    val_dataset,
    batch_size=batch_size,
    shuffle=False,
    num_workers=num_workers,
    pin_memory=torch.cuda.is_available(),
    persistent_workers=(num_workers > 0),
    prefetch_factor=2 if num_workers > 0 else None
    )

    test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False,
    num_workers=num_workers,
    pin_memory=torch.cuda.is_available(),
    persistent_workers=(num_workers > 0),
    prefetch_factor=2 if num_workers > 0 else None
    )

    print("\nEXPANDED DATASET LOADER")
    print("----------------------")
    print("Data root:", DATA_ROOT)
    print("Manifest:", MANIFEST_PATH)
    print("Classes:", len(class_names))
    print("Training images:", len(train_dataset))
    print("Validation images:", len(val_dataset))
    print("Test images:", len(test_dataset))
    print("Total images:", len(df))

    return (
        train_loader,
        val_loader,
        test_loader,
        class_names,
        class_to_idx
    )


# --------------------------------------------------
# BASIC LOADING TEST
# --------------------------------------------------

if __name__ == "__main__":

    loaders = get_expanded_dataloaders(
        batch_size=8,
        num_workers=0
    )

    train_loader = loaders[0]

    images, labels = next(iter(train_loader))

    print("\nIMAGE LOADING TEST")
    print("n------------------")
    print("Batch image shape:", tuple(images.shape))
    print("Batch label shape:", tuple(labels.shape))
    print("Image loading successful.")
