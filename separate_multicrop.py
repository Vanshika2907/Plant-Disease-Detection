
from pathlib import Path
import shutil
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = PROJECT_ROOT.parent / "dataset_cleaning" / "final_split_manifest.csv"

OUTPUT_DIR = PROJECT_ROOT.parent / "MultiCrop_Separated"

# Read manifest
df = pd.read_csv(MANIFEST_PATH)

# Select only MultiCrop images
df = df[df["source"] == "MultiCrop"].copy()

copied = 0
missing = 0

for _, row in df.iterrows():

    source_path = Path(row["location"])

    # Split crop and condition from class name
    class_parts = row["class"].split("___", 1)

    if len(class_parts) != 2:
        print(f"Skipping invalid class: {row['class']}")
        continue

    crop = class_parts[0]
    condition = class_parts[1]

    split = row["final_split"]

    # Create destination:
    # MultiCrop_Separated/Crop/Class/Split/
    destination_folder = (
        OUTPUT_DIR / crop / condition / split
    )

    destination_folder.mkdir(parents=True, exist_ok=True)

    destination_path = destination_folder / source_path.name

    if not source_path.exists():
        print(f"Missing: {source_path}")
        missing += 1
        continue

    if not destination_path.exists():
        shutil.copy2(source_path, destination_path)
        copied += 1

print("\nSeparation completed!")
print(f"Images copied: {copied}")
print(f"Missing images: {missing}")
print(f"Output folder: {OUTPUT_DIR}")

# Summary by crop and class
print("\nImages organised by class:")
summary = df.groupby(["class", "final_split"]).size().unstack(fill_value=0)
print(summary.to_string())

summary = df.groupby(["class", "final_split"]).size().unstack(fill_value=0)
print(summary.to_string())
