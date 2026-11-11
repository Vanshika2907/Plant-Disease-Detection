from pathlib import Path
import json
import sys
import math

import pandas as pd
import torch
from PIL import Image, ImageDraw

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model
from src.expanded_dataset import get_expanded_dataloaders

MODEL_PATH = PROJECT_ROOT / "models" / "mobilenetv2_68_best.pth"
MAPPING_PATH = PROJECT_ROOT / "models" / "class_mapping_68.json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "groundnut_sigatoka_comparison"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

GROUNDNUT = "Groundnut___Early_Leaf_Spot"
BANANA = "Banana___Sigatoka"
BATCH_SIZE = 32
MAX_PER_GROUP = 60
DEVICE = (
    torch.device("cuda") if torch.cuda.is_available()
    else torch.device("mps") if hasattr(torch.backends, "mps")
    and torch.backends.mps.is_available()
    else torch.device("cpu")
)

def save_contact_sheets(records, dataset, group_name):
    if not records:
        print(f"No records for {group_name}")
        return

    # Limit to a deterministic sample so the sheets remain manageable.
    records = records[:MAX_PER_GROUP]
    cell_w, cell_h = 300, 235
    columns, per_page = 3, 30

    for page_start in range(0, len(records), per_page):
        page = records[page_start:page_start + per_page]
        rows = math.ceil(len(page) / columns)
        sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
        draw = ImageDraw.Draw(sheet)

        for i, item in enumerate(page):
            image = dataset._load_image(item["location"])
            image.thumbnail((190, 180))
            col, row = i % columns, i // columns
            x0, y0 = col * cell_w, row * cell_h
            x = x0 + (cell_w - image.width) // 2
            sheet.paste(image, (x, y0 + 3))

            source = str(item.get("source", "unknown"))
            filename = Path(str(item["location"]).split("/")[-1]).name
            pred = str(item["predicted_class"]).replace("___", "/")
            conf = float(item["prediction_confidence"])
            draw.text((x0 + 7, y0 + 188), f"{source[:35]}", fill="black")
            draw.text((x0 + 7, y0 + 204), f"{filename[:35]}", fill="black")
            draw.text((x0 + 7, y0 + 220), f"Pred: {pred[:25]} ({conf:.2f})", fill="black")

        page_num = page_start // per_page + 1
        out = OUTPUT_DIR / f"{group_name}_contact_sheet_{page_num:02d}.jpg"
        sheet.save(out, quality=92)
        print(f"Saved: {out}")

def main():
    if not MODEL_PATH.exists() or not MAPPING_PATH.exists():
        raise FileNotFoundError("68-class model or class mapping file is missing.")

    with open(MAPPING_PATH, "r") as f:
        saved_mapping = json.load(f)

    model = get_model(
        "mobilenetv2",
        num_classes=len(saved_mapping),
        pretrained=False,
        freeze_backbone=False,
    )
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()

    _, _, test_loader, class_names, class_to_idx = get_expanded_dataloaders(
        batch_size=BATCH_SIZE,
        num_workers=0,
    )
    if saved_mapping != class_to_idx:
        raise ValueError("Model mapping and dataset mapping do not match.")

    if GROUNDNUT not in class_to_idx or BANANA not in class_to_idx:
        raise ValueError("Could not find the expected class names in the dataset mapping.")

    test_df = test_loader.dataset.dataframe.reset_index(drop=True)
    groundnut_idx, banana_idx = class_to_idx[GROUNDNUT], class_to_idx[BANANA]
    correct_groundnut, all_banana = [], []
    offset = 0

    print(f"Device: {DEVICE}")
    print("Comparing correctly classified Groundnut Early Leaf Spot with actual Banana Sigatoka...")

    with torch.no_grad():
        for images, labels in test_loader:
            logits = model(images.to(DEVICE))
            probs = torch.softmax(logits, dim=1)
            confs, preds = probs.max(dim=1)

            labels = labels.numpy()
            preds = preds.cpu().numpy()
            confs = confs.cpu().numpy()

            for j, (actual, predicted) in enumerate(zip(labels, preds)):
                if int(actual) == groundnut_idx and int(predicted) == groundnut_idx:
                    row = test_df.iloc[offset + j].to_dict()
                    row.update(actual_class=GROUNDNUT,
                               predicted_class=class_names[int(predicted)],
                               prediction_confidence=float(confs[j]))
                    correct_groundnut.append(row)

                if int(actual) == banana_idx:
                    row = test_df.iloc[offset + j].to_dict()
                    row.update(actual_class=BANANA,
                               predicted_class=class_names[int(predicted)],
                               prediction_confidence=float(confs[j]))
                    all_banana.append(row)

            offset += len(labels)

    # Stable ordering by location makes the selected subset reproducible.
    correct_groundnut.sort(key=lambda x: str(x["location"]))
    all_banana.sort(key=lambda x: str(x["location"]))

    pd.DataFrame(correct_groundnut).to_csv(
        OUTPUT_DIR / "correct_groundnut_early_leaf_spot.csv", index=False
    )
    pd.DataFrame(all_banana).to_csv(
        OUTPUT_DIR / "all_actual_banana_sigatoka.csv", index=False
    )

    print(f"\nCorrect Groundnut Early Leaf Spot examples: {len(correct_groundnut)}")
    print(f"Actual Banana Sigatoka examples: {len(all_banana)}")
    print(f"Showing up to {MAX_PER_GROUP} examples per group in contact sheets.")

    save_contact_sheets(correct_groundnut, test_loader.dataset, "correct_groundnut")
    save_contact_sheets(all_banana, test_loader.dataset, "actual_banana_sigatoka")

    print(f"\nComparison files saved in: {OUTPUT_DIR}")
    print("No dataset files, labels, or model weights were modified.")

if __name__ == "__main__":
    main()
