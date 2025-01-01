# Loan Approval Prediction Web App

This project is a simple web application developed using Streamlit to predict the approval of bank loans. The app takes user input regarding personal and financial details and uses a pre-trained machine learning model to predict loan approval outcomes.

## Overview
The application uses a user-friendly interface to collect information such as age, income, marital status, education, credit history, and existing debt. Based on the input, the application provides instant feedback on loan approval predictions.

## Features
- **Interactive Interface:** Users can input data using sliders and dropdown menus.
- **Real-time Prediction:** The app gives immediate results after submitting the form.
- **Pre-trained Model:** Utilizes a machine learning model (`eniyi.joblib`) for prediction.
- **User Feedback:** Displays approval or rejection messages based on prediction results.

## Requirements
Ensure you have the following dependencies installed:

- Python 3.7+
- Streamlit
- Joblib
- Numpy

Install dependencies using:
```bash
pip install streamlit joblib numpy
```

## Installation and Usage
1. Clone this repository or download the source files.
2. Place the model file (`eniyi.joblib`) in the project directory.
3. Run the application:
```bash
streamlit run app.py
```
4. Open the provided local URL in your browser to interact with the app.

## Model Details
- The app uses a machine learning model saved as `eniyi.joblib`. Ensure this file exists in the project directory.
- The model was trained to predict loan approvals based on features such as age, income, marital status, education, credit history, and existing debt.

## Notes
- The model file `eniyi.joblib` must be pre-trained and compatible with the input structure described in the app.
- The app is designed for demonstration purposes and may require further adjustments for production use.
- Modify the mapping dictionaries for income, marital status, education, and credit history as per your model's training data.

### Example Input
- **Age:** 24
- **Income:** Medium
- **Marital Status:** Single
- **Education:** University
- **Credit History:** Good
- **Existing Debt:** 1000

### Prediction Example
- **Approved Message:** "The Loan is APPROVED!"
- **Rejected Message:** "The Loan is NOT APPROVED!"

