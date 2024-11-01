### Medical Cost Prediction Project

## Project Overview

This project is designed to give people a quick idea of what their medical insurance might cost, based on personal details like age, BMI, smoking status, and more. I built a machine learning model to make these predictions, so users can get an estimate of their expenses and understand what factors could be affecting their insurance costs.

## Dataset Used
I used the Medical Cost Personal Dataset for this project, but I made a few tweaks to focus on the most relevant data:

 Age: The person’s age.

 Sex: Gender (which I encoded for easier model processing).
 
 BMI: Body Mass Index, an indicator of body fat.

 Children: Number of dependent children.

 Smoker: Whether the person smokes (encoded as well).
 
 Charges: The actual medical insurance cost—this is what the model is trained to predict.

Note: The region column was excluded from the analysis, as it wasn’t necessary for this project.

## How to Run the Project
# To run the Medical Cost Prediction project, follow these steps:

1. Download the Project Files:

Begin by downloading the project files from GitHub. Visit the repository link and click on the "Code" button, then select "Download ZIP" to obtain the files. After downloading, unzip the file to access the project folder.

2.Open the Project Directory:

Navigate to the folder where you extracted the project files. This folder contains all the necessary components for the project.

3. Install Required Libraries:

To run the project successfully, you need to install specific Python libraries. These libraries are listed in a file named requirements.txt, which is located in the project folder. Open your command prompt or terminal and use the appropriate method to install these libraries, ensuring that you have Python and pip installed on your machine.

4. Run the Jupyter Notebook:
Open Jupyter Notebook, which is used for data exploration and model training. If you don’t have Jupyter installed, you can install it via Anaconda or pip. Once Jupyter is open in your
web browser, locate the file named insurace.ipynb. Open this notebook and execute each cell to perform data analysis and train the model.

5. Launch the Streamlit Application:
After completing the notebook, you can run the Streamlit application to interact with the model. Find and open the file named app.py. Running this file will start the Streamlit app in your web browser, providing an interface for user interaction.

6. Input Your Details:

When the Streamlit app is open, you will see a form where you can enter personal information such as age, BMI, smoking status, and the number of dependent children. Fill in these details and submit the form to receive a predicted medical insurance cost based on your inputs.
