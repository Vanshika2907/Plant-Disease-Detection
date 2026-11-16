"""
Plant Disease Detection — Streamlit App
Run:  streamlit run streamlit_app/app.py
"""

import json
import sys
from pathlib import Path

import streamlit as st
import torch
import torch.nn.functional as F
import numpy as np
from PIL import Image
from torchvision import transforms, models
import torch.nn as nn
import matplotlib.pyplot as plt
import cv2

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import IMG_SIZE, IMAGENET_MEAN, IMAGENET_STD, get_plant_and_condition


from knowledge_base import get_knowledge


# ============================================================
# MODEL BUILDER
# ============================================================

def build_mobilenetv2(num_classes):
    model = models.mobilenet_v2(weights=None)
    in_features = model.classifier[1].in_features

    model.classifier = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(in_features, 512),
        nn.ReLU(inplace=True),
        nn.Dropout(0.2),
        nn.Linear(512, num_classes),
    )
    return model


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_CONFIGS = {
    "38-class Baseline": {
        "model_file": "mobilenetv2_best.pth",
        "mapping_file": "class_mapping.json",
        "classes": 38,
        "accuracy": "97.29%",
        "description": "Original PlantVillage model",
    },
    "68-class Expanded": {
        "model_file": "mobilenetv2_68_best.pth",
        "mapping_file": "class_mapping_68.json",
        "classes": 68,
        "accuracy": "94.59%",
        "description": "Expanded multi-dataset model",
    },
}


def normalize_mapping(mapping):
    """
    Accept either:
    {"0": "Apple___healthy", ...}
    or:
    {"Apple___healthy": 0, ...}

    Return a consistent index-to-class mapping.
    """
    if not isinstance(mapping, dict):
        raise ValueError("Invalid class mapping format.")

    if not mapping:
        raise ValueError("Class mapping is empty.")

    first_key = next(iter(mapping))

    if str(first_key).isdigit():
        return {str(k): str(v) for k, v in mapping.items()}

    return {
        str(index): str(class_name)
        for class_name, index in mapping.items()
    }


# ============================================================
# MODEL LOADING
# ============================================================

@st.cache_resource
def load_model(model_option):

    config = MODEL_CONFIGS[model_option]

    model_path = PROJECT_ROOT / "models" / config["model_file"]
    mapping_path = PROJECT_ROOT / "models" / config["mapping_file"]

    if not model_path.exists():
        return None, None, f"Model file not found: {model_path}"

    if not mapping_path.exists():
        return None, None, f"Class mapping not found: {mapping_path}"

    try:
        with open(mapping_path, "r", encoding="utf-8") as f:
            raw_mapping = json.load(f)

        idx_to_class = normalize_mapping(raw_mapping)

        if len(idx_to_class) != config["classes"]:
            raise ValueError(
                f"Expected {config['classes']} classes, "
                f"but mapping contains {len(idx_to_class)}."
            )

        device = torch.device(
            "mps" if torch.backends.mps.is_available()
            else "cuda" if torch.cuda.is_available()
            else "cpu"
        )

        model = build_mobilenetv2(len(idx_to_class))

        state_dict = torch.load(
            model_path,
            map_location=device,
            weights_only=True
        )

        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()

        return model, idx_to_class, None

    except Exception as e:
        return None, None, f"Could not load model: {str(e)}"


# ============================================================
# PREDICTION
# ============================================================

def predict(model, image, idx_to_class, device):

    transform = transforms.Compose([
        transforms.Resize(int(IMG_SIZE * 1.14)),
        transforms.CenterCrop(IMG_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=IMAGENET_MEAN,
            std=IMAGENET_STD
        ),
    ])

    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = F.softmax(output, dim=1)[0]

    top_probs, top_indices = probabilities.topk(
        min(5, len(idx_to_class))
    )

    results = []

    for probability, index in zip(top_probs, top_indices):

        class_name = idx_to_class[str(index.item())]
        plant, condition = get_plant_and_condition(class_name)

        results.append({
            "class_name": class_name,
            "plant": plant,
            "condition": condition,
            "probability": probability.item(),
        })

    return results, input_tensor


# ============================================================
# GRAD-CAM
# ============================================================

def generate_gradcam(model, input_tensor, pred_class_idx):

    model.eval()

    target_layer = model.features[-1]

    activations = []
    gradients = []

    forward_hook = target_layer.register_forward_hook(
        lambda module, inputs, output:
        activations.append(output.detach())
    )

    backward_hook = target_layer.register_full_backward_hook(
        lambda module, grad_input, grad_output:
        gradients.append(grad_output[0].detach())
    )

    try:
        output = model(input_tensor)
        model.zero_grad()

        output[0, pred_class_idx].backward()

        weights = gradients[0].mean(
            dim=(2, 3),
            keepdim=True
        )

        cam = torch.relu(
            (weights * activations[0]).sum(dim=1)
        ).squeeze().cpu().numpy()

        cam = (
            (cam - cam.min()) /
            (cam.max() - cam.min() + 1e-8)
        )

        return cv2.resize(cam, (IMG_SIZE, IMG_SIZE))

    finally:
        forward_hook.remove()
        backward_hook.remove()


# ============================================================
# USER INTERFACE
# ============================================================

def main():

    st.set_page_config(
        page_title="Plant Health Classification",
        page_icon="🌿",
        layout="wide"
    )

    st.title("Plant Health Condition Classification")

    st.markdown(
        "Upload a leaf image to obtain an AI-generated visual "
        "classification of its possible health condition."
    )

    # ---------------- SIDEBAR ----------------

    with st.sidebar:

        st.header("Settings")

        model_option = st.selectbox(
            "Select Model",
            list(MODEL_CONFIGS.keys()),
            help="Choose between the original 38-class model "
                 "and the expanded 68-class model."
        )

        show_gradcam = st.checkbox(
            "Show Grad-CAM heatmap",
            value=True
        )

        config = MODEL_CONFIGS[model_option]

        st.markdown("---")
        st.subheader("Model Information")

        st.markdown(f"**Architecture:** MobileNetV2")
        st.markdown(f"**Classes:** {config['classes']}")
        st.markdown(f"**Test Accuracy:** {config['accuracy']}")
        st.markdown(f"**Model:** {config['description']}")

        st.markdown("---")
        st.caption(
            "Predictions are based on visual patterns in the "
            "training datasets. They are not confirmed biological "
            "diagnoses."
        )

    # ---------------- LOAD MODEL ----------------

    model, idx_to_class, error = load_model(model_option)

    if error:
        st.error(error)
        return

    device = next(model.parameters()).device

    # ---------------- SUPPORTED CROPS ----------------

    plants = sorted({
        get_plant_and_condition(class_name)[0]
        for class_name in idx_to_class.values()
    })

    # ---------------- MAIN LAYOUT ----------------

    col1, col2 = st.columns(2, gap="large")

    uploaded = None
    image = None

    with col1:

        st.subheader("Upload Leaf Image")

        uploaded = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"],
            help="Use a clear, well-lit image of a leaf."
        )

        if uploaded:

            try:
                image = Image.open(uploaded).convert("RGB")

                st.image(
                    image,
                    caption="Uploaded image",
                    use_container_width=True
                )

            except Exception:
                st.error("Could not read this image.")
                return

    if not uploaded:

        with col2:

            st.subheader("Classification Results")

            st.info("Upload a leaf image to get started.")

            st.markdown("**Tips for better predictions:**")
            st.markdown("- Use a clear, well-lit photograph.")
            st.markdown("- Keep the leaf visible.")
            st.markdown("- Avoid blurry images.")
            st.markdown("- Avoid heavy shadows.")

            st.markdown("---")
            st.markdown("**Supported crops and plants**")

            st.write(", ".join(plants))

        return

    # ---------------- RUN PREDICTION ----------------

    with st.spinner("Analysing image..."):

        results, input_tensor = predict(
            model,
            image,
            idx_to_class,
            device
        )

    top = results[0]

    # Use the complete crop + condition key to avoid mixing diseases
    # that share a condition name across different crops.
    info = get_knowledge(top["class_name"])

    # ---------------- DISPLAY RESULTS ----------------

    with col2:

        st.subheader("Classification Results")

        st.markdown(
            f"### {top['plant']} — {top['condition']}"
        )

        st.metric(
            "Top prediction softmax score",
            f"{top['probability']:.1%}",
            help="This is the model softmax output, not a calibrated probability or a confirmed likelihood of disease."
        )
        st.caption(
            "Softmax scores indicate the model's relative output for its classes; "
            "they are not calibrated diagnostic probabilities."
        )

        if info:
            st.info(
                "Educational decision-support information only. "
                "The image classification is not a confirmed diagnosis."
            )

            st.markdown(f"**Classification category:** {info['type'].replace('_', ' ').title()}")

            st.markdown("**Visible symptoms**")
            for item in info["symptoms"]:
                st.write(f"- {item}")

            if info["causal_agent"]:
                st.markdown(f"**Causal agent:** {info['causal_agent']}")
            else:
                st.markdown("**Causal agent:** Not established in this knowledge-base entry.")

            st.markdown("**Spread / transmission**")
            for item in info["spread"]:
                st.write(f"- {item}")

            st.markdown("**General management**")
            for item in info["management"]:
                st.write(f"- {item}")

            st.markdown("**Prevention**")
            for item in info["prevention"]:
                st.write(f"- {item}")

            if info["nutrient_guidance"]:
                st.markdown(f"**Nutrient guidance:** {info['nutrient_guidance']}")

            st.markdown(f"**Treatment note:** {info['treatment_note']}")
            st.caption(info["diagnostic_caution"])
            if info["review_status"] != "VERIFIED":
                st.warning(
                    "Knowledge-base content is a preliminary educational draft and has not yet been fully source-verified. "
                    "Do not use it as a standalone diagnosis or treatment instruction."
                )
                if info["sources"]:
                    st.markdown("**Reference sources**")

                    for source in info["sources"]:
                        organization = source.get("organization", "Source")
                        title = source.get("title", "Reference")
                        url = source.get("url")

                        if url:
                            st.markdown(
                                f"- **{organization}** — "
                                f"[{title}]({url})"
                            )
                        else:
                            st.write(f"- **{organization}** — {title}")

                else:
                    st.caption(
                        "No independently verified references have been attached "
                        "to this entry yet."
                    )

            if info["chemical_treatment"] is not None:
                st.warning(
                    "A chemical treatment entry is present. Verify the current "
                    "Indian registration and exact product label before use."
                )
                st.write(info["chemical_treatment"])
            else:
                st.caption("No chemical treatment recommendation is provided.")
        else:
            st.warning(
                "No knowledge-base entry matches this exact model class. "
                "Please consult an agricultural specialist."
            )

        # ---------------- TOP 5 ----------------

        st.markdown("---")
        st.markdown("#### Top 5 Predictions")

        fig, ax = plt.subplots(figsize=(7, 2.8))

        labels = [
            f"{r['plant']} — {r['condition']}"
            for r in results
        ]

        probabilities = [
            r["probability"] for r in results
        ]

        colors = [
            "#2ecc71" if i == 0 else "#bdc3c7"
            for i in range(len(labels))
        ]

        ax.barh(
            range(len(labels)),
            probabilities,
            color=colors,
            edgecolor="white"
        )

        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels, fontsize=8)
        ax.set_xlabel("Prediction probability")
        ax.set_xlim(0, 1)
        ax.invert_yaxis()
        ax.grid(axis="x", alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # ---------------- GRAD-CAM ----------------

    if show_gradcam:

        st.markdown("---")
        st.subheader("Grad-CAM — Model Attention Visualisation")

        pred_idx = next(
            int(index)
            for index, class_name in idx_to_class.items()
            if class_name == top["class_name"]
        )

        with st.spinner("Generating Grad-CAM..."):

            cam = generate_gradcam(
                model,
                input_tensor,
                pred_idx
            )

        img_resized = image.resize((IMG_SIZE, IMG_SIZE))

        heatmap = plt.cm.jet(cam)[:, :, :3]

        overlay = (
            0.5 * np.array(img_resized) / 255.0
            + 0.5 * heatmap
        ).clip(0, 1)

        gc1, gc2, gc3 = st.columns(3)

        with gc1:

            st.image(
                img_resized,
                caption="Original image",
                use_container_width=True
            )

        with gc2:

            fig2, ax2 = plt.subplots()

            ax2.imshow(cam, cmap="jet")
            ax2.axis("off")
            ax2.set_title("Attention map")

            st.pyplot(fig2)
            plt.close(fig2)

        with gc3:

            st.image(
                (overlay * 255).astype(np.uint8),
                caption="Grad-CAM overlay",
                use_container_width=True
            )

        st.caption(
            "Grad-CAM highlights image regions that contributed "
            "to the selected prediction. It does not prove that "
            "the model identified a disease-specific lesion."
        )

    # ---------------- FOOTER ----------------

    st.markdown("---")

    st.caption(
        f"Active model: {model_option} | "
        f"Number of classes: {len(idx_to_class)}"
    )


if __name__ == "__main__":
    main()
