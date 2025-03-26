# Student Forecaster

This repository is used by the team **Student Forecaster**, part of the **Le Wagon bootcamp**. The model aims to predict whether a student will pass or fail based on their socio-economic conditions.

## Toolset

- **oh-my-zsh**
- **Visual Studio Code**
- **git**
- **streamlit**

## Description

The academic performance of a student depends not only on their academic capabilities but also their socio-economic status. This model helps predict whether a student will pass or fail based on factors such as family background, education level, and more.

### Imagine this...

You are a headmaster/headmistress, managing a school of thousands of students. How do you create the ideal environment for students to academically excel in their education?

**ET VOILA!**

The **Student Forecaster Model** provides insights on how socio-economic conditions impact academic success.

## How it works

The model has been trained on historical data of students and uses machine learning techniques to predict whether a student will pass or fail. Here are some details about the model and performance:

### Models Used

| Model                      | Precision | Test vs Train Precision CV | Over/Underfitting |
| -------------------------- | --------- | -------------------------- | ------------------ |
| Logistic Regression         | 0.75      | 0.72 vs 0.72               | No Overfitting     |
| KNN KNeighborsClassifier    | 0.76      | 0.67 vs 0.83               | Overfitting        |
| Random Forest Classifier    | 0.81      | 0.70 vs 0.98               | Overfitting        |
| XGB Classifier              | 0.82      | 0.68 vs 0.95               | Overfitting        |
| Gradient Boosting Classifier| 0.76      | 0.70 vs 0.78               | Slightly Overfitting|

### Performance Metrics

- **Accuracy**: 0.77
- **Precision**: 0.76
- **Recall**: 0.90
- **F1 Score**: 0.82

## Live Demo

You can interact with the model through the live demo hosted on Streamlit:

[Student Forecaster - Live Demo](https://student-forecaster.streamlit.app/)

## Requirements

The required Python packages are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

## Usage 

Run the model and Streamlit app with the following command
```bash
streamlit run Student_Forecaster.py
```
## Additional Resources

For a detailed explanation:
1. Of the analysis, check out the [presentation slides](presentation.slides.html).
2. Of the model, check out the [Jupyter Notebook](presentation.ipynb).