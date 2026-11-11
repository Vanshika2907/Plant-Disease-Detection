# Plant Health Condition Classification from Leaf Images Using Deep Learning

A deep learning-based plant health classification system that identifies visible plant conditions from leaf images using MobileNetV2. The project combines transfer learning, image classification, model explainability using Grad-CAM, and an interactive Streamlit web application.

The project includes an original 38-class baseline model and an expanded 68-class model developed using datasets from multiple sources.

## 1. Project Overview

Plant diseases, pest-related damage, and abiotic conditions can affect crop health and agricultural productivity. Identifying visible symptoms from leaf images can support preliminary plant-health assessment.

This project uses deep learning to classify plant leaf images into healthy and affected categories. Users can upload images through a Streamlit application and view predicted classes, confidence scores, top-five predictions, and Grad-CAM visualisations.

Two MobileNetV2 model versions are available:

- **38-class Baseline:** Trained using the original PlantVillage dataset.
- **68-class Expanded Model:** Trained using a combined dataset containing PlantVillage, Groundnut Karnataka, MultiCrop, and Maize images.

The system recognises visual patterns in leaf images. Its predictions should not be treated as confirmed pathogen diagnoses.

## 2. Problem Statement

Identifying plant-health conditions through visual inspection can be challenging because different diseases, pests, and environmental conditions may produce similar symptoms.

The project aims to develop an image-based classification system that recognises visible plant-health conditions across multiple crops and presents its predictions through an accessible web application.

## 3. Project Objectives

- Develop deep learning models for plant-health image classification.
- Apply transfer learning using MobileNetV2.
- Expand classification coverage using datasets from multiple sources.
- Evaluate model performance using accuracy, precision, recall, and F1-score.
- Examine performance across different dataset sources.
- Integrate the models into a Streamlit application.
- Provide visual explanations using Grad-CAM.

## 4. Dataset Description

The project uses four image sources for the expanded classification model.

| Dataset source | Eligible images |
|---|---:|
| PlantVillage | 54,284 |
| Groundnut Karnataka | 10,351 |
| MultiCrop | 21,571 |
| Maize | 320 |
| **Total** | **86,526** |

The final expanded dataset contains **68 classes** covering healthy and affected plant conditions.

### Dataset characteristics

| Characteristic | Description |
|---|---|
| Total images | 86,526 |
| Total classes | 68 |
| Crop coverage | Multiple crops |
| Image format | RGB |
| Model input dimensions | 224 × 224 |
| Dataset type | Labelled leaf images |
| Duplicate handling | Exact duplicate images removed |
| Split strategy | Training, validation, and testing |

### Final Dataset Split

| Split | Images |
|---|---:|
| Training | 60,027 |
| Validation | 13,693 |
| Testing | 12,806 |
| **Total** | **86,526** |

The dataset was cleaned to remove duplicate copies and exclude selected classes that were not considered suitable for the final classification taxonomy. Exact duplicate image hashes were checked across the final splits.

The final dataset was organised into 68 eligible classes. Some classes were flagged for manual review because of potential visual or source-related inconsistencies.

### Dataset Sources

- **PlantVillage:** A labelled collection of plant leaf images covering multiple crops and disease categories.
- **Groundnut Karnataka:** Groundnut images covering healthy leaves, early and late leaf spot, rust, early rust, and nutrition deficiency.
- **MultiCrop:** Images covering Banana, Cauliflower, Chilli, Groundnut, and Radish conditions.
- **Maize:** Images covering healthy leaves, Maize Streak Virus, Maize Lethal Necrosis, and Northern Leaf Blight.

The Maize Exserohilum turcicum category was mapped to Northern Leaf Blight, the disease associated with that pathogen.

## 5. Methodology

The project follows these stages:

1. **Data collection:** Gather labelled leaf images from the four dataset sources.
2. **Data cleaning:** Verify image files, remove exact duplicates, and identify classes requiring exclusion or review.
3. **Class organisation:** Consolidate overlapping categories into a consistent 68-class taxonomy.
4. **Data splitting:** Prepare training, validation, and testing sets while preserving the specified source assignments.
5. **Preprocessing:** Resize images to 224 × 224 pixels and apply image normalisation.
6. **Model development:** Use MobileNetV2 with transfer learning.
7. **Model training:** Train and fine-tune the expanded classification model.
8. **Evaluation:** Measure performance using classification metrics and source-wise analysis.
9. **Application integration:** Deploy model selection and image prediction through Streamlit.
10. **Explainability:** Generate Grad-CAM visualisations to inspect influential image regions.

## 6. Model Development and Training

### MobileNetV2 Architecture

MobileNetV2 is a lightweight convolutional neural network designed for efficient image classification. It uses depthwise separable convolutions, inverted residual blocks, and linear bottlenecks to reduce computational requirements.

Transfer learning was used in both model versions. Pretrained MobileNetV2 weights served as the feature extraction backbone, with a modified classification layer for the required number of classes.

### Model Versions

| Feature | Baseline | Expanded |
|---|---:|---:|
| Architecture | MobileNetV2 | MobileNetV2 |
| Number of classes | 38 | 68 |
| Main dataset | PlantVillage | Four combined sources |
| Input dimensions | 224 × 224 | 224 × 224 |
| Training approach | Transfer learning and fine-tuning | Transfer learning and fine-tuning |

### Expanded Model Training Strategy

The expanded model was trained for 20 epochs.

- Initial training phase: The backbone was frozen while the classification head was trained.
- Fine-tuning phase: Selected later backbone layers were unfrozen and trained along with the classification head.

The best-performing checkpoint was selected using validation performance.

## 7. Results and Performance Evaluation

### 7.1 Original 38-Class Baseline

The original model achieved the following results:

| Evaluation metric | Result |
|---|---:|
| Test Accuracy | 97.29% |
| Macro F1-score | 0.96 |
| Weighted F1-score | 0.97 |
| Number of classes | 38 |
| Test images | 8,146 |

These results belong to the original PlantVillage-based evaluation and should not be interpreted as results from the expanded model.

### 7.2 Expanded 68-Class Model

The expanded model was evaluated on a separate test set containing 12,806 images.

| Evaluation metric | Result |
|---|---:|
| Test Accuracy | 94.59% |
| Macro F1-score | 0.9109 |
| Weighted F1-score | 0.9485 |
| Number of classes | 68 |
| Test images | 12,806 |

The best validation accuracy achieved during training was 94.64%.

### 7.3 Source-Wise Evaluation

The expanded model was additionally evaluated across the four dataset sources.

| Dataset source | Test images | Accuracy |
|---|---:|---:|
| PlantVillage | 8,143 | 95.78% |
| Groundnut Karnataka | 2,451 | 91.92% |
| MultiCrop | 2,164 | 93.02% |
| Maize | 48 | 100.00% |

The Maize result is based on only 48 test images and should not be interpreted as evidence of perfect generalisation.

Source-wise analysis also identified differences in the classification of Groundnut Early Leaf Spot images between the Groundnut Karnataka and MultiCrop sources. This indicates that image-source characteristics may influence model predictions and requires further investigation.

### Performance Metrics

- **Accuracy:** Proportion of correctly classified test images.
- **Precision:** Proportion of predictions for a class that are correct.
- **Recall:** Proportion of actual images of a class correctly identified.
- **F1-score:** Harmonic mean of precision and recall.

Macro F1 gives equal importance to each class, whereas weighted F1 accounts for the number of samples in each class.

## 8. Streamlit Web Application

The trained models are integrated into an interactive application developed using Streamlit.

### Application Features

- **Model Selection:** Switch between the 38-class baseline and 68-class expanded model.
- **Image Upload:** Upload a plant leaf image for classification.
- **Condition Prediction:** Display the predicted plant-health category.
- **Confidence Score:** Display the model's softmax confidence score.
- **Top-5 Predictions:** Display the five highest-scoring predicted classes.
- **Plant Information:** Display available information for supported categories.
- **Grad-CAM Visualisation:** Inspect image regions influencing the model's prediction.

### Application Screenshots

**Screenshot 1 – Main Application**

![Main Application](screenshot-app1.png)

**Screenshot 2 – Prediction and Results**

![Prediction Results](screenshot-app2.png)

## 9. Model Explainability Using Grad-CAM

Grad-CAM (Gradient-weighted Class Activation Mapping) is an explainability technique used to visualise image regions that contribute to a model's prediction.

The application provides three visual outputs:

1. **Original Image:** The uploaded plant leaf image.
2. **Heatmap:** Highlights regions that contribute to the prediction.
3. **Overlay:** Combines the heatmap with the original image.

Grad-CAM helps users inspect which image regions influenced the model's output. However, it does not establish that the highlighted regions correspond to the biological cause of a condition.

## 10. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyTorch | Deep learning framework |
| MobileNetV2 | Image classification architecture |
| Torchvision | Pretrained models and image transformations |
| NumPy | Numerical operations |
| Pandas | Dataset and evaluation analysis |
| Matplotlib | Visualisation |
| Grad-CAM | Model explainability |
| Streamlit | Web application |
| Git and GitHub | Version control and project hosting |

## 11. Project Structure

```text
Plant-Disease-Detection-main/
│
├── models/
│   ├── class_mapping.json
│   ├── class_mapping_68.json
│   ├── mobilenetv2_best.pth
│   └── mobilenetv2_68_best.pth
│
├── outputs/
│   ├── mobilenetv2_68_classification_report.txt
│   ├── mobilenetv2_68_confusion_matrix.csv
│   ├── mobilenetv2_68_history.json
│   ├── mobilenetv2_68_per_class_metrics.csv
│   ├── mobilenetv2_68_test_summary.json
│   ├── groundnut_sigatoka_comparison/
│   ├── groundnut_sigatoka_diagnostic/
│   └── source_wise_evaluation/
│
├── src/
│   ├── config.py
│   ├── dataset.py
│   ├── expanded_dataset.py
│   ├── model.py
│   ├── train.py
│   ├── train_expanded.py
│   ├── evaluate.py
│   ├── evaluate_expanded.py
│   ├── evaluate_by_source.py
│   ├── compare_groundnut_banana.py
│   └── diagnose_groundnut_sigatoka.py
│
├── streamlit_app/
│   └── app.py
│
├── .gitignore
├── download_data.py
├── separate_multicrop.py
├── requirements.txt
├── README.md
├── LICENSE
├── screenshot-app1.png
└── screenshot-app2.png
```

## 12. Installation and Execution

### Prerequisites

- Python installed on your system.
- Git installed on your system.
- Required project dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vanshika2907/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

```bash
python -m streamlit run streamlit_app/app.py
```

The application will open in your browser.

Both trained model checkpoints and their corresponding class mappings must be present in the `models/` directory.

The original training datasets are not included in the repository. They must be obtained separately before reproducing the training process.

## 13. Live Application

The project has an earlier Streamlit Community Cloud deployment.

**Live Demo:** https://plant-disease-detection-bio.streamlit.app/

The deployment should be updated and tested with the expanded model files before it is considered a live demonstration of the latest 68-class version.

## 14. Limitations

- The datasets contain images collected from different sources and environments. Their visual characteristics may differ.
- Test images come from sources represented in the training data; therefore, the evaluation does not establish generalisation to completely unseen image sources.
- Performance on real-world field images may differ from the reported test results.
- Some classes have relatively small test samples, making their individual performance metrics less stable.
- The dataset contains some classes requiring further manual verification.
- The model identifies visual patterns and does not confirm the presence of a pathogen.
- Confidence scores do not guarantee prediction correctness.
- Grad-CAM visualisations indicate influential image regions but do not establish biological causation.

The application should be treated as an educational and preliminary decision-support tool, not a replacement for professional plant-health diagnosis.

## 15. Future Scope

- Evaluate the model using independently collected field images.
- Investigate the influence of image-source characteristics on classification performance.
- Improve the representation of classes with limited samples.
- Expand and validate plant-condition information in the application.
- Explore additional architectures and compare their performance.
- Investigate model optimisation for resource-constrained devices.
- Explore mobile application integration.

## 16. Development Approach and Codebase Attribution

This project was developed using an existing open-source repository as its starting framework.

**Original Repository:** https://github.com/moadil65/Plant-Disease-Detection

The original repository provided the initial project framework and application structure. The team extended the project through additional dataset preparation, model training, evaluation, classification expansion, source-wise analysis, and modifications to the Streamlit application.

The original repository is acknowledged for its contribution to the initial project framework.

## 17. References

1. Hughes, D. P., & Salathé, M. (2015). *An open access repository of images on plant health to enable the development of mobile disease diagnostics*. arXiv:1511.08060.
2. Sandler, M., et al. (2018). *MobileNetV2: Inverted Residuals and Linear Bottlenecks*. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
3. Selvaraju, R. R., et al. (2017). *Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization*.
4. PyTorch Documentation: https://pytorch.org/docs/
5. Streamlit Documentation: https://docs.streamlit.io/
6. Roboflow Universe – MultiCrop Disease Dataset: https://universe.roboflow.com/multicrop-disease/custom-workflow-object-detection-2nqxa
