from pathlib import Path
import json
import sys
import math

import pandas as pd
import torch
from PIL import Image, ImageDraw
from torchvision import transforms

# Make the project root available for imports.
SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model
from src.expanded_dataset import get_expanded_dataloaders

MODEL_PATH = PROJECT_ROOT / "models" / "mobilenetv2_68_best.pth"
MAPPING_PATH = PROJECT_ROOT / "models" / "class_mapping_68.json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "groundnut_sigatoka_diagnostic"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_TRUE = "Groundnut___Early_Leaf_Spot"
TARGET_PREDICTED = "Banana___Sigatoka"
BATCH_SIZE = 32
DEVICE = (
    torch.device("cuda") if torch.cuda.is_available()
    else torch.device("mps") if hasattr(torch.backends, "mps")
    and torch.backends.mps.is_available()
    else torch.device("cpu")
)

def main():
    if not MODEL_PATH.exists() or not MAPPING_PATH.exists():
        raise FileNotFoundError("The 68-class model or class mapping file is missing.")

    with open(MAPPING_PATH, "r") as f:
        saved_mapping = json.load(f)

    model = get_model(
        "mobilenetv2",
        num_classes=len(saved_mapping),
        pretrained=False,
        freeze_backbone=False,
    )
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    model.load_state_dict(checkpoint)
    model.to(DEVICE)
    model.eval()

    _, _, test_loader, class_names, class_to_idx = get_expanded_dataloaders(
        batch_size=BATCH_SIZE,
        num_workers=0,
    )

    if saved_mapping != class_to_idx:
        raise ValueError("Model mapping and dataset mapping do not match.")

    if TARGET_TRUE not in class_to_idx or TARGET_PREDICTED not in class_to_idx:
        raise ValueError(
            "Target class name not found. Check the exact names in class_mapping_68.json."
        )

    true_idx = class_to_idx[TARGET_TRUE]
    predicted_idx = class_to_idx[TARGET_PREDICTED]
    test_df = test_loader.dataset.dataframe.reset_index(drop=True)

    rows = []
    offset = 0

    print(f"Device: {DEVICE}")
    print("Scanning the complete test set for Groundnut Early Leaf Spot → Banana Sigatoka...")

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(DEVICE)
            probabilities = torch.softmax(model(images), dim=1)
            confidences, predictions = probabilities.max(dim=1)

            labels_np = labels.cpu().numpy()
            predictions_np = predictions.cpu().numpy()
            confidences_np = confidences.cpu().numpy()

            for j, (actual, predicted) in enumerate(zip(labels_np, predictions_np)):
                if int(actual) == true_idx and int(predicted) == predicted_idx:
                    row = test_df.iloc[offset + j].to_dict()
                    row["actual_class"] = TARGET_TRUE
                    row["predicted_class"] = TARGET_PREDICTED
                    row["prediction_confidence"] = float(confidences_np[j])
                    rows.append(row)

            offset += len(labels_np)

    result_df = pd.DataFrame(rows)
    csv_path = OUTPUT_DIR / "groundnut_early_leaf_spot_predicted_as_banana_sigatoka.csv"
    result_df.to_csv(csv_path, index=False)

    print(f"\nMatching errors found: {len(result_df)}")
    print(f"Misclassification list saved: {csv_path}")

    if result_df.empty:
        print("No matching errors were found. Check the target class names and evaluation split.")
        return

    # Use the dataset's own ZIP-aware image reader so both ZIP and normal paths work.
    image_reader = test_loader.dataset
    thumb_w, thumb_h = 180, 180
    cell_w, cell_h = 300, 230
    columns = 3
    per_page = 36

    for page_start in range(0, len(result_df), per_page):
        page = result_df.iloc[page_start:page_start + per_page]
        rows_per_page = math.ceil(len(page) / columns)
        sheet = Image.new(
            "RGB",
            (columns * cell_w, rows_per_page * cell_h),
            "white",
        )
        draw = ImageDraw.Draw(sheet)

        for local_i, (_, record) in enumerate(page.iterrows()):
            image = image_reader._load_image(record["location"])
            image.thumbnail((thumb_w, thumb_h))

            col = local_i % columns
            row_num = local_i // columns
            x0 = col * cell_w
            y0 = row_num * cell_h

            image_x = x0 + (cell_w - image.width) // 2
            sheet.paste(image, (image_x, y0 + 5))

            source = str(record.get("source", "source not recorded"))
            confidence = float(record["prediction_confidence"])
            filename = Path(str(record["location"]).split("/")[-1]).name

            draw.text((x0 + 8, y0 + 190), f"#{page_start + local_i + 1}  {source[:35]}", fill="black")
            draw.text((x0 + 8, y0 + 207), f"{filename[:38]} | conf: {confidence:.3f}", fill="black")

        image_path = OUTPUT_DIR / f"contact_sheet_{page_start // per_page + 1:02d}.jpg"
        sheet.save(image_path, quality=92)
        print(f"Contact sheet saved: {image_path}")

    print("\nDiagnostic scan complete. Review the contact sheets and CSV before making dataset changes.")

if __name__ == "__main__":
    main()
