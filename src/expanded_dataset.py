from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from collections import Counter
import pandas as pd

import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from torchvision import transforms
from PIL import Image


# Project locations
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BIO_EL_ROOT = PROJECT_ROOT.parent
MANIFEST_PATH = BIO_EL_ROOT / "dataset_cleaning" / "final_split_manifest.csv"

IMG_SIZE = 224


class ExpandedPlantDataset(Dataset):
    def __init__(self, dataframe, class_to_idx, transform=None):
        self.dataframe = dataframe.reset_index(drop=True)
        self.class_to_idx = class_to_idx
        self.transform = transform
        self.zip_paths = {}
        self.zip_handles = {}

    def __len__(self):
        return len(self.dataframe)

    def _find_zip(self, zip_filename):
        if zip_filename not in self.zip_paths:
            matches = list(BIO_EL_ROOT.rglob(zip_filename))
            if not matches:
                raise FileNotFoundError(
                    f"Could not find ZIP archive: {zip_filename}"
                )
            self.zip_paths[zip_filename] = matches[0]

        return self.zip_paths[zip_filename]

    def _load_image(self, location):
        location = str(location)

        # ZIP-based location:
        # archive.zip/internal/folder/image.jpg
        if ".zip/" in location:
            zip_filename, internal_path = location.split(".zip/", 1)
            zip_filename += ".zip"

            if zip_filename not in self.zip_handles:
                zip_path = self._find_zip(zip_filename)
                self.zip_handles[zip_filename] = ZipFile(zip_path, "r")

            image_bytes = self.zip_handles[zip_filename].read(
                internal_path
            )

            image = Image.open(BytesIO(image_bytes)).convert("RGB")

        else:
            image = Image.open(location).convert("RGB")

        return image

    def __getitem__(self, index):
        row = self.dataframe.iloc[index]

        image = self._load_image(row["location"])
        label = self.class_to_idx[row["class"]]

        if self.transform:
            image = self.transform(image)

        return image, label


def get_expanded_dataloaders(
    batch_size=32,
    num_workers=0
):
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"Manifest not found: {MANIFEST_PATH}"
        )

    df = pd.read_csv(MANIFEST_PATH)

    required_columns = {"class", "location", "final_split"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Manifest is missing columns: {missing}")

    # Use only the final, eligible dataset records.
    df = df.dropna(subset=["class", "location", "final_split"])

    class_names = sorted(df["class"].unique().tolist())
    class_to_idx = {
        class_name: index
        for index, class_name in enumerate(class_names)
    }

    if len(class_names) != 68:
        raise ValueError(
            f"Expected 68 classes, but found {len(class_names)}."
        )

    train_df = df[df["final_split"] == "train"].copy()
    val_df = df[df["final_split"] == "validation"].copy()
    test_df = df[df["final_split"] == "test"].copy()

    if min(len(train_df), len(val_df), len(test_df)) == 0:
        raise ValueError("One or more dataset splits are empty.")

    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(IMG_SIZE, scale=(0.8, 1.0)),
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

    train_dataset = ExpandedPlantDataset(
        train_df, class_to_idx, train_transform
    )
    val_dataset = ExpandedPlantDataset(
        val_df, class_to_idx, evaluation_transform
    )
    test_dataset = ExpandedPlantDataset(
        test_df, class_to_idx, evaluation_transform
    )

    # Balance training classes without changing validation/test data.
    train_labels = [
        class_to_idx[name] for name in train_df["class"]
    ]
    class_counts = Counter(train_labels)

    sample_weights = [
        1.0 / class_counts[label] for label in train_labels
    ]

    sampler = WeightedRandomSampler(
        weights=sample_weights,
        num_samples=len(sample_weights),
        replacement=True
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        sampler=sampler,
        num_workers=num_workers,
        pin_memory=torch.cuda.is_available()
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=torch.cuda.is_available()
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=torch.cuda.is_available()
    )

    print("\nEXPANDED DATASET LOADER")
    print("----------------------")
    print(f"Classes: {len(class_names)}")
    print(f"Training images: {len(train_dataset)}")
    print(f"Validation images: {len(val_dataset)}")
    print(f"Test images: {len(test_dataset)}")
    print(f"Total images: {len(df)}")

    return (
        train_loader,
        val_loader,
        test_loader,
        class_names,
        class_to_idx
    )


if __name__ == "__main__":
    loaders = get_expanded_dataloaders(batch_size=8)

    train_loader = loaders[0]
    images, labels = next(iter(train_loader))

    print("\nIMAGE LOADING TEST")
    print("------------------")
    print("Batch image shape:", tuple(images.shape))
    print("Batch label shape:", tuple(labels.shape))
    print("Image loading successful.")
