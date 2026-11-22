
import torch
import torch.nn as nn
from torchvision import models


# --------------------------------------------------
# CLASSIFIER HEAD
# --------------------------------------------------

def build_classifier(in_features, num_classes):
    return nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(in_features, 512),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(512, num_classes)
    )


# --------------------------------------------------
# MOBILENETV2
# --------------------------------------------------

def get_mobilenetv2(
    num_classes=68,
    pretrained=True,
    freeze_backbone=True
):
    weights = (
        models.MobileNet_V2_Weights.DEFAULT
        if pretrained else None
    )

    model = models.mobilenet_v2(weights=weights)

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    in_features = model.classifier[1].in_features
    model.classifier = build_classifier(in_features, num_classes)

    return model


# --------------------------------------------------
# RESNET50
# --------------------------------------------------

def get_resnet50(
    num_classes=68,
    pretrained=True,
    freeze_backbone=True
):
    weights = (
        models.ResNet50_Weights.DEFAULT
        if pretrained else None
    )

    model = models.resnet50(weights=weights)

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    in_features = model.fc.in_features
    model.fc = build_classifier(in_features, num_classes)

    return model


# --------------------------------------------------
# EFFICIENTNETB0
# --------------------------------------------------

def get_efficientnet_b0(
    num_classes=68,
    pretrained=True,
    freeze_backbone=True
):
    weights = (
        models.EfficientNet_B0_Weights.DEFAULT
        if pretrained else None
    )

    model = models.efficientnet_b0(weights=weights)

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    in_features = model.classifier[1].in_features
    model.classifier = build_classifier(in_features, num_classes)

    return model


# --------------------------------------------------
# DENSENET121
# --------------------------------------------------

def get_densenet121(
    num_classes=68,
    pretrained=True,
    freeze_backbone=True
):
    weights = (
        models.DenseNet121_Weights.DEFAULT
        if pretrained else None
    )

    model = models.densenet121(weights=weights)

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    in_features = model.classifier.in_features
    model.classifier = build_classifier(in_features, num_classes)

    return model


# --------------------------------------------------
# MODEL FACTORY
# --------------------------------------------------

def get_model(
    model_name,
    num_classes=68,
    pretrained=True,
    freeze_backbone=True
):
    model_name = model_name.lower().replace("-", "").replace("_", "")

    model_builders = {
        "mobilenetv2": get_mobilenetv2,
        "resnet50": get_resnet50,
        "efficientnetb0": get_efficientnet_b0,
        "densenet121": get_densenet121
    }

    if model_name not in model_builders:
        raise ValueError(
            f"Unsupported model: {model_name}. "
            f"Choose from {list(model_builders.keys())}."
        )

    return model_builders[model_name](
        num_classes=num_classes,
        pretrained=pretrained,
        freeze_backbone=freeze_backbone
    )


# --------------------------------------------------
# LAYER UNFREEZING
# --------------------------------------------------

def unfreeze_layers(model, model_name, num_layers=2):
    model_name = model_name.lower().replace("-", "").replace("_", "")

    # MobileNetV2: unfreeze the final feature blocks.
    if model_name == "mobilenetv2":
        blocks = list(model.features.children())

        for block in blocks[-num_layers:]:
            for param in block.parameters():
                param.requires_grad = True

    # EfficientNetB0: unfreeze the final feature blocks.
    elif model_name == "efficientnetb0":
        blocks = list(model.features.children())

        for block in blocks[-num_layers:]:
            for param in block.parameters():
                param.requires_grad = True

    # ResNet50: unfreeze layer4, then layer3, etc.
    elif model_name == "resnet50":
        layers = [
            model.layer4,
            model.layer3,
            model.layer2,
            model.layer1
        ]

        for layer in layers[:num_layers]:
            for param in layer.parameters():
                param.requires_grad = True

    # DenseNet121: progressively unfreeze later feature modules.
    elif model_name == "densenet121":
        layers = [
            model.features.norm5,
            model.features.denseblock4,
            model.features.transition3,
            model.features.denseblock3,
            model.features.transition2,
            model.features.denseblock2
        ]

        for layer in layers[:num_layers]:
            for param in layer.parameters():
                param.requires_grad = True

    else:
        raise ValueError(f"Unsupported model for fine-tuning: {model_name}")


# --------------------------------------------------
# MODEL SUMMARY
# --------------------------------------------------

def model_summary(model):
    total_parameters = sum(
        param.numel() for param in model.parameters()
    )

    trainable_parameters = sum(
        param.numel()
        for param in model.parameters()
        if param.requires_grad
    )

    print("\nMODEL SUMMARY")
    print("------------------------------")
    print(f"Total parameters: {total_parameters:,}")
    print(f"Trainable parameters: {trainable_parameters:,}")
    print(
        f"Frozen parameters: "
        f"{total_parameters - trainable_parameters:,}"
    )
