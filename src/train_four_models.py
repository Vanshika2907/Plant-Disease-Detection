
from pathlib import Path
import json
import time
import sys
import random
import numpy as np

import torch
import torch.nn as nn
from torch.optim import Adam
from torch.optim.lr_scheduler import ReduceLROnPlateau

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent

sys.path.insert(0, str(PROJECT_ROOT))

from src.model import get_model, unfreeze_layers, model_summary
from src.expanded_dataset import get_expanded_dataloaders


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

# Kaggle input is read-only, so save results in working.
if Path("/kaggle/working").exists():
    RUN_ROOT = Path("/kaggle/working")
else:
    RUN_ROOT = PROJECT_ROOT

MODEL_DIR = RUN_ROOT / "models"
OUTPUT_DIR = RUN_ROOT / "outputs"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODELS_TO_TRAIN = [
    ("resnet50", "resnet50_68"),
    ("efficientnet_b0", "efficientnet_b0_68"),
    ("densenet121", "densenet121_68")
]

BATCH_SIZE = 32
TOTAL_EPOCHS = 20
FROZEN_EPOCHS = 3

INITIAL_LR = 1e-3
FINETUNE_LR = 1e-5

PATIENCE = 5
SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
    DEVICE = torch.device("cuda")
elif (
    hasattr(torch.backends, "mps")
    and torch.backends.mps.is_available()
):
    DEVICE = torch.device("mps")
else:
    DEVICE = torch.device("cpu")

USE_MULTI_GPU = (
    DEVICE.type == "cuda"
    and torch.cuda.device_count() > 1
)
# --------------------------------------------------
# CHECKPOINT UTILITIES
# --------------------------------------------------

def save_checkpoint(path, state):

    temporary_path = path.with_suffix(".tmp")

    torch.save(state, temporary_path)
    temporary_path.replace(path)


def load_checkpoint(path):

    try:
        return torch.load(
            path,
            map_location=DEVICE,
            weights_only=False
        )
    except TypeError:
        return torch.load(path, map_location=DEVICE)


def capture_random_states():

    return {
        "python": random.getstate(),
        "numpy": np.random.get_state(),
        "torch": torch.get_rng_state(),
        "cuda": (
            torch.cuda.get_rng_state_all()
            if torch.cuda.is_available()
            else None
        )
    }


def restore_random_states(states):

    random.setstate(states["python"])
    np.random.set_state(states["numpy"])
    torch.set_rng_state(states["torch"])

    if (
        torch.cuda.is_available()
        and states.get("cuda") is not None
    ):
        torch.cuda.set_rng_state_all(states["cuda"])


# --------------------------------------------------
# TRAINING / VALIDATION EPOCH
# --------------------------------------------------

def run_epoch(model, loader, criterion, optimizer=None, scaler=None):

    training = optimizer is not None

    if training:
        model.train()
    else:
        model.eval()

    total_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:

        images = images.to(DEVICE, non_blocking=True)
        labels = labels.to(DEVICE, non_blocking=True)

        if training:
            optimizer.zero_grad(set_to_none=True)

        with torch.set_grad_enabled(training):
            with torch.autocast(
                device_type="cuda",
                dtype=torch.float16,
                enabled=(DEVICE.type == "cuda")
            ):
                outputs = model(images)
                loss = criterion(outputs, labels)

            if training:
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()

        total_loss += loss.item() * images.size(0)

        predictions = outputs.argmax(dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, correct / total

# --------------------------------------------------
# TRAIN ONE MODEL
# --------------------------------------------------

def train_one_model(
    model_name,
    file_prefix,
    train_loader,
    val_loader,
    num_classes
):

    print("\n" + "=" * 60)
    print(f"TRAINING: {model_name.upper()}")
    print("=" * 60)

    model = get_model(
        model_name,
        num_classes=num_classes,
        pretrained=True,
        freeze_backbone=True
    ).to(DEVICE)
    if USE_MULTI_GPU:
        training_model = nn.DataParallel(model)
        print("Using", torch.cuda.device_count(), "GPUs")
    else:
        training_model = model
        print("Using one device:", DEVICE)

    model_summary(model)

    criterion = nn.CrossEntropyLoss()

    best_path = MODEL_DIR / f"{file_prefix}_best.pth"
    latest_path = OUTPUT_DIR / f"{file_prefix}_latest_checkpoint.pth"
    history_path = OUTPUT_DIR / f"{file_prefix}_history.json"

    # --------------------------------------------------
    # RESUME OR START NEW TRAINING
    # --------------------------------------------------

    start_epoch = 0
    best_val_accuracy = 0.0
    best_epoch = 0
    epochs_without_improvement = 0
    history = []
    finetuning_started = False

    if latest_path.exists():

        checkpoint = load_checkpoint(latest_path)

        if checkpoint.get("training_complete", False):

            print("This model has already completed training.")
            print("Best validation accuracy:",
                  checkpoint["best_val_accuracy"] * 100, "%")

            del model
            return {
                "model": model_name,
                "best_validation_accuracy":
                    checkpoint["best_val_accuracy"],
                "best_epoch": checkpoint["best_epoch"],
                "checkpoint": str(best_path)
            }

        print("\nExisting checkpoint found.")
        print("Resuming training...")

        model.load_state_dict(checkpoint["model_state_dict"])

        start_epoch = checkpoint["next_epoch"]
        best_val_accuracy = checkpoint["best_val_accuracy"]
        best_epoch = checkpoint["best_epoch"]
        epochs_without_improvement = checkpoint[
            "epochs_without_improvement"
        ]
        history = checkpoint["history"]
        finetuning_started = checkpoint["finetuning_started"]

    else:
        print("\nStarting new training run.")

    # --------------------------------------------------
    # CREATE CORRECT OPTIMIZER FOR RESUME PHASE
    # --------------------------------------------------

    if finetuning_started:

        unfreeze_layers(
            model,
            model_name,
            num_layers=2
        )

        optimizer = Adam(
            filter(lambda p: p.requires_grad, model.parameters()),
            lr=FINETUNE_LR
        )

    else:

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
    scaler = torch.amp.GradScaler(
    "cuda",
    enabled=(DEVICE.type == "cuda")
    ) 

    if latest_path.exists():

        if finetuning_started or start_epoch < FROZEN_EPOCHS:

            optimizer.load_state_dict(
                checkpoint["optimizer_state_dict"]
            )

            scheduler.load_state_dict(
                checkpoint["scheduler_state_dict"]
            )
            if "scaler_state_dict" in checkpoint:
                scaler.load_state_dict(checkpoint["scaler_state_dict"])

        # Restore random states after model and optimizer setup.
        restore_random_states(checkpoint["random_states"])

    # --------------------------------------------------
    # TRAINING LOOP
    # --------------------------------------------------

    for epoch in range(start_epoch, TOTAL_EPOCHS):

        # Switch to fine-tuning after the frozen phase.
        if epoch == FROZEN_EPOCHS and not finetuning_started:

            print("\nUnfreezing final backbone blocks...")

            unfreeze_layers(
                model,
                model_name,
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

            finetuning_started = True

            print("Fine-tuning optimizer initialized.")

        start_time = time.time()

        train_loss, train_accuracy = run_epoch(
            training_model,
            train_loader,
            criterion,
            optimizer,
            scaler
        )

        val_loss, val_accuracy = run_epoch(
            training_model,
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

        # Save best validation model.
        if val_accuracy > best_val_accuracy:

            best_val_accuracy = val_accuracy
            best_epoch = epoch + 1
            epochs_without_improvement = 0

            temporary_best = best_path.with_suffix(".tmp")
            torch.save(model.state_dict(), temporary_best)
            temporary_best.replace(best_path)

            print("  Best checkpoint saved.")

        else:
            epochs_without_improvement += 1

        # Save training history.
        with history_path.open("w") as f:
            json.dump(history, f, indent=4)

        # Save complete resumable checkpoint after every epoch.
        checkpoint_state = {
            "model_name": model_name,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "scaler_state_dict": scaler.state_dict(),
            "next_epoch": epoch + 1,
            "best_val_accuracy": best_val_accuracy,
            "best_epoch": best_epoch,
            "epochs_without_improvement":
                epochs_without_improvement,
            "finetuning_started": finetuning_started,
            "history": history,
            "random_states": capture_random_states(),
            "training_complete": False
        }

        save_checkpoint(latest_path, checkpoint_state)

        print("  Resumable checkpoint saved.")

        # Early stopping after the frozen phase.
        if (
            epoch >= FROZEN_EPOCHS
            and epochs_without_improvement >= PATIENCE
        ):

            print("\nEarly stopping triggered.")
            break

    # --------------------------------------------------
    # MARK TRAINING COMPLETE
    # --------------------------------------------------

    final_checkpoint = load_checkpoint(latest_path)
    final_checkpoint["training_complete"] = True

    save_checkpoint(latest_path, final_checkpoint)

    print("\n" + "-" * 50)
    print(f"{model_name.upper()} TRAINING FINISHED")
    print("-" * 50)

    print(f"Best validation accuracy: {best_val_accuracy * 100:.2f}%")
    print(f"Best epoch: {best_epoch}")
    print(f"Best model: {best_path}")
    print(f"Latest resumable checkpoint: {latest_path}")
    print(f"History: {history_path}")

    del model

    if DEVICE.type == "mps":
        torch.mps.empty_cache()
    elif DEVICE.type == "cuda":
        torch.cuda.empty_cache()

    return {
        "model": model_name,
        "best_validation_accuracy": best_val_accuracy,
        "best_epoch": best_epoch,
        "checkpoint": str(best_path)
    }


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    print("=" * 60)
    print("THREE-ARCHITECTURE TRAINING")
    print("=" * 60)

    print("Device:", DEVICE)
    print("Output directory:", OUTPUT_DIR)

    print("\nLoading common 68-class dataset...")

    (
        train_loader,
        val_loader,
        test_loader,
        class_names,
        class_to_idx
    ) = get_expanded_dataloaders(
        batch_size=BATCH_SIZE,
        num_workers=2
    )

    num_classes = len(class_names)

    if num_classes != 68:
        raise ValueError(
            f"Expected 68 classes, found {num_classes}."
        )

    # Check the original class mapping.
    source_mapping = PROJECT_ROOT / "models" / "class_mapping_68.json"
    output_mapping = MODEL_DIR / "class_mapping_68.json"

    if source_mapping.exists():

        with source_mapping.open() as f:
            saved_mapping = json.load(f)

        if saved_mapping != class_to_idx:
            raise ValueError(
                "Existing 68-class mapping differs from dataset mapping."
            )

        print("Existing class mapping verified.")

    elif output_mapping.exists():

        with output_mapping.open() as f:
            saved_mapping = json.load(f)

        if saved_mapping != class_to_idx:
            raise ValueError("Class mapping mismatch.")

        print("Output class mapping verified.")

    else:

        with output_mapping.open("w") as f:
            json.dump(class_to_idx, f, indent=4)

        print("Class mapping saved.")

    print(f"\nNumber of classes: {num_classes}")
    print(f"Training images: {len(train_loader.dataset)}")
    print(f"Validation images: {len(val_loader.dataset)}")
    print(f"Test images: {len(test_loader.dataset)}")

    results = []

    for model_name, file_prefix in MODELS_TO_TRAIN:

        result = train_one_model(
            model_name,
            file_prefix,
            train_loader,
            val_loader,
            num_classes
        )

        results.append(result)

        with (OUTPUT_DIR / "three_model_training_summary.json").open("w") as f:
            json.dump(results, f, indent=4)

    print("\n" + "=" * 60)
    print("ALL THREE TRAINING RUNS FINISHED")
    print("=" * 60)

    for result in results:
        print(
            f"{result['model']}: "
            f"{result['best_validation_accuracy'] * 100:.2f}% "
            f"(epoch {result['best_epoch']})"
        )

    print("\nThe test set was not used for model selection.")


if __name__ == "__main__":
    main()
