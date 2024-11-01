### Medical Cost Prediction
### Project Overview

This project leverages machine learning to build a regression model that accurately predicts medical expenses based on individual characteristics. The model is trained on the Medical Cost Personal Dataset, and the app is built with Streamlit for an interactive user experience.

## Project Structure
## Dataset

Source: Kaggle (Medical Cost Personal Dataset)
Features Used:
age: Age of the patient
sex: Gender (encoded)
bmi: Body Mass Index (BMI)
children: Number of dependents
smoker: Smoking status (encoded)
Note: The region column was excluded from the analysis.
## Exploratory Data Analysis (EDA)
Initial analysis involves understanding the distribution of variables, identifying correlations, and gaining insights into the dataset.
## Data Pre-Processing

## Feature Encoding: Categorical features like gender and smoker status are encoded to numerical values suitable for modeling.
## Data Cleaning: Handling missing values.
## Model Training & Evaluation

Model Selection: Linear regression is chosen as the predictive model due to its interpretability and suitability for regression tasks.
Training: The model is trained on the pre-processed data to learn relationships between features and insurance costs.
Evaluation: Performance metrics such as R-squared are used to assess the model's accuracy on both training and test datasets.
Building a Predictive System

Deployment: Using the trained model to build a predictive system that can estimate insurance costs based on input data (age, gender, BMI, etc.).

## Files in the Repository
#app.py: Streamlit application file.
#requirements.txt: Lists dependencies for the project.
#model_lin.pkl: Serialized linear regression model.
#insurace_cost_prediction.ipynb: Jupyter notebook containing Python code for the project, including data exploration, preprocessing, model training, evaluation, and deployment.
#README.md: Overview of the project and instructions for running the code, along with contact information.

## Instructions for Running the Code
Prerequisites: Ensure necessary libraries like pandas, numpy, scikit-learn are installed.
Clone Repository: Clone the repository to your local machine.
Run Jupyter Notebooks: Open and run insurance_cost_prediction.ipynb in the specified order to replicate the analysis, model training, and deployment.
