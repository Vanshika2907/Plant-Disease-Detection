from pathlib import Path
import json
import sys

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model
from src.expanded_dataset import get_expanded_dataloaders

MODEL_PATH = PROJECT_ROOT / "models" / "mobilenetv2_68_best.pth"
MAPPING_PATH = PROJECT_ROOT / "models" / "class_mapping_68.json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "source_wise_evaluation"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BATCH_SIZE = 32
DEVICE = (
    torch.device("cuda") if torch.cuda.is_available()
    else torch.device("mps") if hasattr(torch.backends, "mps")
    and torch.backends.mps.is_available()
    else torch.device("cpu")
)


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    if not MAPPING_PATH.exists():
        raise FileNotFoundError(f"Class mapping not found: {MAPPING_PATH}")

    with open(MAPPING_PATH, "r", encoding="utf-8") as f:
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
        raise ValueError("Saved model mapping does not match the expanded dataset mapping.")

    test_df = test_loader.dataset.dataframe.reset_index(drop=True)
    required_columns = {"source", "class", "location"}
    missing = required_columns - set(test_df.columns)
    if missing:
        raise ValueError(f"Test manifest is missing required columns: {sorted(missing)}")

    y_true_all, y_pred_all, confidence_all = [], [], []
    offset = 0

    print(f"Device: {DEVICE}")
    print("Running inference on the test set only...")

    with torch.no_grad():
        for images, labels in test_loader:
            logits = model(images.to(DEVICE))
            probabilities = torch.softmax(logits, dim=1)
            confidences, predictions = probabilities.max(dim=1)

            batch_size = len(labels)
            y_true_all.extend(labels.numpy().astype(int).tolist())
            y_pred_all.extend(predictions.cpu().numpy().astype(int).tolist())
            confidence_all.extend(confidences.cpu().numpy().astype(float).tolist())
            offset += batch_size

    if len(test_df) != len(y_true_all):
        raise ValueError(
            f"Manifest/test-loader mismatch: {len(test_df)} rows vs "
            f"{len(y_true_all)} predictions."
        )

    results = test_df.copy()
    results["actual_index"] = y_true_all
    results["predicted_index"] = y_pred_all
    results["actual_class"] = results["actual_index"].map(
        {i: name for name, i in class_to_idx.items()}
    )
    results["predicted_class"] = results["predicted_index"].map(
        {i: name for name, i in class_to_idx.items()}
    )
    results["prediction_confidence"] = confidence_all
    results["correct"] = results["actual_index"] == results["predicted_index"]

    predictions_path = OUTPUT_DIR / "source_wise_test_predictions.csv"
    results.to_csv(predictions_path, index=False)

    source_rows = []
    class_rows = []

    for source, group in results.groupby("source", dropna=False):
        y_true = group["actual_index"].to_numpy(dtype=int)
        y_pred = group["predicted_index"].to_numpy(dtype=int)
        labels_present = np.unique(y_true)

        source_rows.append({
            "source": str(source),
            "test_images": int(len(group)),
            "actual_classes": int(len(labels_present)),
            "accuracy": float(accuracy_score(y_true, y_pred)),
            "macro_f1_present_classes": float(
                f1_score(y_true, y_pred, labels=labels_present,
                         average="macro", zero_division=0)
            ),
            "weighted_f1": float(
                f1_score(y_true, y_pred, labels=labels_present,
                         average="weighted", zero_division=0)
            ),
            "correct": int((y_true == y_pred).sum()),
            "incorrect": int((y_true != y_pred).sum()),
        })

        precision, recall, f1, support = precision_recall_fscore_support(
            y_true, y_pred, labels=labels_present, zero_division=0
        )
        for idx, p, r, f, n in zip(labels_present, precision, recall, f1, support):
            class_rows.append({
                "source": str(source),
                "class": class_names[int(idx)],
                "support": int(n),
                "precision": float(p),
                "recall": float(r),
                "f1": float(f),
            })

    source_summary = pd.DataFrame(source_rows).sort_values("source")
    class_metrics = pd.DataFrame(class_rows).sort_values(["source", "class"])

    summary_path = OUTPUT_DIR / "source_wise_summary.csv"
    class_path = OUTPUT_DIR / "source_wise_class_metrics.csv"
    source_summary.to_csv(summary_path, index=False)
    class_metrics.to_csv(class_path, index=False)

    overall = {
        "test_images": int(len(results)),
        "accuracy": float(accuracy_score(results["actual_index"], results["predicted_index"])),
        "macro_f1": float(f1_score(
            results["actual_index"], results["predicted_index"],
            average="macro", zero_division=0
        )),
        "weighted_f1": float(f1_score(
            results["actual_index"], results["predicted_index"],
            average="weighted", zero_division=0
        )),
        "note": (
            "Source-wise metrics describe performance on sources represented in the "
            "existing test split. They do not measure generalisation to a wholly unseen source."
        ),
    }
    with open(OUTPUT_DIR / "overall_check.json", "w", encoding="utf-8") as f:
        json.dump(overall, f, indent=2)

    print("\nSOURCE-WISE EVALUATION FINISHED")
    print("=" * 55)
    print(source_summary.to_string(index=False))
    print("\nOverall check:")
    print(f"Test images: {overall['test_images']}")
    print(f"Accuracy:    {overall['accuracy']:.4%}")
    print(f"Macro F1:    {overall['macro_f1']:.4f}")
    print(f"Weighted F1: {overall['weighted_f1']:.4f}")
    print("\nFiles saved:")
    print(summary_path)
    print(class_path)
    print(predictions_path)
    print(OUTPUT_DIR / "overall_check.json")
    print("\nNo model weights, dataset images, labels, or split assignments were changed.")


if __name__ == "__main__":
    main()
