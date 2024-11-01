# Import necessary libraries
import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
with open('model_lin.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app interface
st.title('🏥 Medical Charges Prediction App')


st.write("""
### Enter the details below to predict the Medical Charges:
""")

# Get user input for all necessary features
# User input
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", options=["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["yes", "no"])

# Convert inputs
sex = 0 if sex == "male" else 1
smoker = 1 if smoker == "yes" else 0
# Create a DataFrame for prediction
input_data = np.array([[age,sex,bmi,children,smoker]])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Medical Costs: ${prediction[0]:,.2f}")