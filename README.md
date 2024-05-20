# Deep Learning Classifier Project

This project implements a deep learning classifier for font recognition using PyTorch. It involves preprocessing images, extracting text boxes, and classifying the fonts using a convolutional neural network (CNN).

## Files
- 'fonts` : Folder where .ttf files of font-styles are stored.
- `font_classifier.ipynb`: Jupyter Notebook containing the implementation and explanation of the classifier.
- `training_data/`: Directory containing the dataset images for training.
- `models/model.py`: Python script defining the CNN model architecture.
-  `output_images` : Test images for multiple bounding boxes
- `requirements.txt`: File listing the required Python packages for running the project.

## Requirements

- Python 3.8.10
- torch==2.0.0+cu118
- torchvision==0.15.1+cu118
- opencv-python==4.8.1.78
- pillow==9.50
- pytesseract==0.3.10
- numpy==1.24.3
- scikit-learn==1.2.2
- matplotlib==3.7.1
- tqdm==4.66.1
- seaborn==0.12.2


## Instructions

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/deep-learning-classifier.git
```
2. Navigate to the project directory:

```bash
cd deep-learning-classifier
```
Install the required packages using pip:

```bash 
pip install -r requirements.txt
```
3. Launch Jupyter Notebook:

```bash
jupyter notebook font_classifier.ipynb
```
Follow the instructions in the notebook to execute each cell and train/test the classifier.

