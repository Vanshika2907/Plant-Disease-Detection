from pathlib import Path
import json
import time

import torch
import torch.nn as nn
from torch.optim import Adam
from torch.optim.lr_scheduler import ReduceLROnPlateau

import sys

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent

sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model, unfreeze_layers
from src.expanded_dataset import get_expanded_dataloaders


# ---------------- CONFIGURATION ----------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "mobilenetv2_68"
BATCH_SIZE = 32
TOTAL_EPOCHS = 20
FROZEN_EPOCHS = 3
INITIAL_LR = 1e-3
FINETUNE_LR = 1e-5
PATIENCE = 5
SEED = 42

torch.manual_seed(SEED)

if torch.cuda.is_available():
    DEVICE = torch.device("cuda")
elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
else:
    DEVICE = torch.device("cpu")


# ---------------- TRAINING FUNCTIONS ----------------

def run_epoch(model, loader, criterion, optimizer=None):
    training = optimizer is not None
    model.train() if training else model.eval()

    total_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images = images.to(DEVICE)
        labels = labels.to(DEVICE)

        if training:
            optimizer.zero_grad()

        with torch.set_grad_enabled(training):
            outputs = model(images)
            loss = criterion(outputs, labels)

            if training:
                loss.backward()
                optimizer.step()

        total_loss += loss.item() * images.size(0)
        predictions = outputs.argmax(dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, correct / total


def main():
    print("DEVICE:", DEVICE)
    print("Preparing expanded dataset...")

    train_loader, val_loader, test_loader, class_names, class_to_idx = (
        get_expanded_dataloaders(
            batch_size=BATCH_SIZE,
            num_workers=0
        )
    )

    num_classes = len(class_names)

    # Save the expanded class mapping separately.
    mapping_path = MODEL_DIR / "class_mapping_68.json"

    with open(mapping_path, "w") as f:
        json.dump(class_to_idx, f, indent=4)

    print(f"\nNumber of classes: {num_classes}")
    print("Creating MobileNetV2...")

    model = get_model(
        "mobilenetv2",
        num_classes=num_classes,
        pretrained=True,
        freeze_backbone=True
    )

    model = model.to(DEVICE)

    criterion = nn.CrossEntropyLoss()

    optimizer = Adam(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=INITIAL_LR
    )

    scheduler = ReduceLROnPlateau(
        optimizer,
        mode="max",
        factor=0.5,
        patience=2
    )

    best_val_accuracy = 0.0
    epochs_without_improvement = 0
    history = []

    checkpoint_path = MODEL_DIR / f"{MODEL_NAME}_best.pth"
    history_path = OUTPUT_DIR / f"{MODEL_NAME}_history.json"

    print("\nStarting training...")
    print("----------------------------------------")

    for epoch in range(TOTAL_EPOCHS):

        # Fine-tune the last two feature blocks after the frozen phase.
        if epoch == FROZEN_EPOCHS:
            print("\nUnfreezing the last two MobileNetV2 feature blocks...")

            unfreeze_layers(
                model,
                "mobilenetv2",
                num_layers=2
            )

            optimizer = Adam(
                filter(lambda p: p.requires_grad, model.parameters()),
                lr=FINETUNE_LR
            )

            scheduler = ReduceLROnPlateau(
                optimizer,
                mode="max",
                factor=0.5,
                patience=2
            )

        start_time = time.time()

        train_loss, train_accuracy = run_epoch(
            model,
            train_loader,
            criterion,
            optimizer
        )

        val_loss, val_accuracy = run_epoch(
            model,
            val_loader,
            criterion
        )

        scheduler.step(val_accuracy)

        elapsed = time.time() - start_time

        print(
            f"Epoch [{epoch + 1}/{TOTAL_EPOCHS}] "
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_accuracy * 100:.2f}% | "
            f"Val Loss: {val_loss:.4f} | "
            f"Val Acc: {val_accuracy * 100:.2f}% | "
            f"Time: {elapsed:.1f}s"
        )

        history.append({
            "epoch": epoch + 1,
            "train_loss": train_loss,
            "train_accuracy": train_accuracy,
            "validation_loss": val_loss,
            "validation_accuracy": val_accuracy
        })

        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            epochs_without_improvement = 0

            torch.save(model.state_dict(), checkpoint_path)

            print("  Best checkpoint saved.")
        else:
            epochs_without_improvement += 1

        with open(history_path, "w") as f:
            json.dump(history, f, indent=4)

        # Allow the fine-tuning phase to run before early stopping.
        if (
            epoch >= FROZEN_EPOCHS
            and epochs_without_improvement >= PATIENCE
        ):
            print("\nEarly stopping: validation accuracy did not improve.")
            break

    print("\n----------------------------------------")
    print("TRAINING FINISHED")
    print("----------------------------------------")
    print(f"Best validation accuracy: {best_val_accuracy * 100:.2f}%")
    print(f"Model saved: {checkpoint_path}")
    print(f"Class mapping saved: {mapping_path}")
    print(f"Training history saved: {history_path}")
    print("\nThe test set has NOT been used for model selection.")


if __name__ == "__main__":
    main()
