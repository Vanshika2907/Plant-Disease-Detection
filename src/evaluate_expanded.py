
from pathlib import Path
import json
import sys

import numpy as np
import pandas as pd
import torch

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

# Make the project root available for imports.
SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent

sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model
from src.expanded_dataset import get_expanded_dataloaders


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

MODEL_DIR = PROJECT_ROOT / "models"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

MODEL_PATH = MODEL_DIR / "mobilenetv2_68_best.pth"
MAPPING_PATH = MODEL_DIR / "class_mapping_68.json"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if torch.cuda.is_available():
    DEVICE = torch.device("cuda")
elif (
    hasattr(torch.backends, "mps")
    and torch.backends.mps.is_available()
):
    DEVICE = torch.device("mps")
else:
    DEVICE = torch.device("cpu")


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

def load_model():

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    if not MAPPING_PATH.exists():
        raise FileNotFoundError(f"Class mapping not found: {MAPPING_PATH}")

    with open(MAPPING_PATH, "r") as f:
        class_to_idx = json.load(f)

    num_classes = len(class_to_idx)

    if num_classes != 68:
        raise ValueError(
            f"Expected 68 classes, found {num_classes}."
        )

    model = get_model(
        "mobilenetv2",
        num_classes=num_classes,
        pretrained=False,
        freeze_backbone=False
    )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE
    )

    model.load_state_dict(checkpoint)
    model = model.to(DEVICE)
    model.eval()

    idx_to_class = {
        int(index): name
        for name, index in class_to_idx.items()
    }

    return model, class_to_idx, idx_to_class


# --------------------------------------------------
# EVALUATION
# --------------------------------------------------

def main():

    print("=" * 50)
    print("68-CLASS MODEL EVALUATION")
    print("=" * 50)

    print(f"Device: {DEVICE}")

    model, saved_mapping, idx_to_class = load_model()

    print("\nLoading test dataset...")

    _, _, test_loader, class_names, class_to_idx = (
        get_expanded_dataloaders(
            batch_size=32,
            num_workers=0
        )
    )

    # Verify that model and dataset use identical class indices.
    if saved_mapping != class_to_idx:
        raise ValueError(
            "Saved model mapping does not match dataset mapping. "
            "Evaluation stopped to prevent incorrect class labels."
        )

    print("Class mapping verification passed.")
    print(f"Test images: {len(test_loader.dataset)}")

    all_predictions = []
    all_labels = []

    print("\nRunning inference on test set...")
    print("-" * 50)

    with torch.no_grad():

        for batch_idx, (images, labels) in enumerate(test_loader):

            images = images.to(DEVICE)

            outputs = model(images)
            predictions = outputs.argmax(dim=1)

            all_predictions.extend(
                predictions.cpu().numpy()
            )

            all_labels.extend(
                labels.numpy()
            )

            if (batch_idx + 1) % 50 == 0:
                processed = min(
                    (batch_idx + 1) * test_loader.batch_size,
                    len(test_loader.dataset)
                )

                print(
                    f"Processed {processed}/"
                    f"{len(test_loader.dataset)} images"
                )

    y_true = np.array(all_labels)
    y_pred = np.array(all_predictions)

    # --------------------------------------------------
    # OVERALL METRICS
    # --------------------------------------------------

    accuracy = accuracy_score(y_true, y_pred)

    macro_f1 = f1_score(
        y_true,
        y_pred,
        average="macro",
        zero_division=0
    )

    weighted_f1 = f1_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    print("\n" + "=" * 50)
    print("OVERALL TEST RESULTS")
    print("=" * 50)

    print(f"Test images:       {len(y_true)}")
    print(f"Test accuracy:     {accuracy * 100:.2f}%")
    print(f"Macro F1:          {macro_f1:.4f}")
    print(f"Weighted F1:       {weighted_f1:.4f}")

    # --------------------------------------------------
    # CLASSIFICATION REPORT
    # --------------------------------------------------

    report = classification_report(
        y_true,
        y_pred,
        labels=list(range(len(class_names))),
        target_names=class_names,
        zero_division=0
    )

    print("\n" + "=" * 50)
    print("CLASSIFICATION REPORT")
    print("=" * 50)

    print(report)

    report_path = (
        OUTPUT_DIR / "mobilenetv2_68_classification_report.txt"
    )

    with open(report_path, "w") as f:
        f.write("68-CLASS MOBILENETV2 TEST EVALUATION\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Test images: {len(y_true)}\n")
        f.write(f"Test accuracy: {accuracy * 100:.2f}%\n")
        f.write(f"Macro F1: {macro_f1:.4f}\n")
        f.write(f"Weighted F1: {weighted_f1:.4f}\n\n")
        f.write("CLASSIFICATION REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(report)

    # --------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------

    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=list(range(len(class_names)))
    )

    cm_df = pd.DataFrame(
        cm,
        index=class_names,
        columns=class_names
    )

    cm_path = (
        OUTPUT_DIR / "mobilenetv2_68_confusion_matrix.csv"
    )

    cm_df.to_csv(cm_path)

    # --------------------------------------------------
    # PER-CLASS METRICS
    # --------------------------------------------------

    report_dict = classification_report(
        y_true,
        y_pred,
        labels=list(range(len(class_names))),
        target_names=class_names,
        output_dict=True,
        zero_division=0
    )

    per_class = []

    for class_name in class_names:

        metrics = report_dict[class_name]

        per_class.append({
            "class": class_name,
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1-score"],
            "support": metrics["support"]
        })

    per_class_df = pd.DataFrame(per_class)

    per_class_df = per_class_df.sort_values(
        "f1_score",
        ascending=True
    )

    per_class_path = (
        OUTPUT_DIR / "mobilenetv2_68_per_class_metrics.csv"
    )

    per_class_df.to_csv(
        per_class_path,
        index=False
    )

    print("\n" + "=" * 50)
    print("10 LOWEST F1 CLASSES")
    print("=" * 50)

    print(
        per_class_df.head(10).to_string(index=False)
    )

    print("\n" + "=" * 50)
    print("10 HIGHEST F1 CLASSES")
    print("=" * 50)

    print(
        per_class_df.tail(10)
        .sort_values("f1_score", ascending=False)
        .to_string(index=False)
    )

    # --------------------------------------------------
    # SAVE SUMMARY
    # --------------------------------------------------

    summary = {
        "model": "MobileNetV2",
        "num_classes": len(class_names),
        "test_images": len(y_true),
        "test_accuracy": float(accuracy),
        "macro_f1": float(macro_f1),
        "weighted_f1": float(weighted_f1)
    }

    summary_path = (
        OUTPUT_DIR / "mobilenetv2_68_test_summary.json"
    )

    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=4)

    # --------------------------------------------------
    # FINISHED
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("EVALUATION FINISHED")
    print("=" * 50)

    print(f"Test accuracy: {accuracy * 100:.2f}%")
    print(f"Macro F1:      {macro_f1:.4f}")
    print(f"Weighted F1:   {weighted_f1:.4f}")

    print("\nFiles saved:")
    print(report_path)
    print(cm_path)
    print(per_class_path)
    print(summary_path)


if __name__ == "__main__":
    main()
