import streamlit as st
import joblib
import numpy as np

# En iyi modeli yükleme
model = joblib.load('eniyi.joblib')  # Bu dosyanın var olduğundan emin olun

# Uygulama başlığı
st.title("Bank Loan Approval Prediction")

# Kullanıcıdan veri alma
st.subheader("Please enter your information")

# Yaş (18-65 arası)
age = st.slider("Age", 18, 65, 24)

# Gelir Durumu (Low, Medium, High)
income = st.selectbox("Income", ["Low", "Medium", "High"])

# Medeni Durum (Single, Married)
marital_status = st.selectbox("Marital Status", ["Single", "Married"])

# Eğitim Durumu (High School, University)
education = st.selectbox("Education", ["High School", "University"])

# Kredi Geçmişi (Good, Bad)
credit_history = st.selectbox("Credit History", ["Good", "Bad"])

# Mevcut Borç Durumu (0-5000 arasında)
existing_debt = st.slider("Existing Debt", 0, 5000, 1000)

# Kullanıcı verilerini sayısal değerlere dönüştürme
income_map = {"Low": 0, "Medium": 1, "High": 2}
marital_status_map = {"Single": 0, "Married": 1}
education_map = {"High School": 0, "University": 1}
credit_history_map = {"Bad": 0, "Good": 1}

# Verileri modelin anlayacağı sayısal formatta hazırlama
input_data = [
    age,
    income_map[income],
    marital_status_map[marital_status],
    education_map[education],
    credit_history_map[credit_history],
    existing_debt
]

# Buton ile tahmin yapma
if st.button("Predict"):
    
    # Modelin tahmin yapması
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)

    # Tahminin sonucun gösterilmesi
    if prediction[0] == 1:
        st.success("The Loan is APPROVED!")
    else:
        st.error("The Loan is NOT APPROVED!")
