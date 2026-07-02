# 🏠 House Price Prediction

A machine learning web app that predicts house prices based on property and neighborhood features, built with XGBoost.

## 🔍 Overview
This project predicts house prices using the classic Boston Housing dataset (sourced from Kaggle), trained with an XGBoost Regressor. Users can adjust sliders for features like crime rate, number of rooms, and pupil-teacher ratio to get an instant price prediction.

## 🛠️ Tech Stack
- **Model:** XGBoost Regressor
- **Dataset:** Boston Housing Dataset (Kaggle)
- **Frontend:** Streamlit
- **Libraries:** scikit-learn, xgboost, pandas, numpy

## 📊 Features Used
CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT

## 📊 Performance
- [Training R squared error : 0.949514930331503
Training Mean absolute error : 1.4501344062314176
Test R squared error : 0.9256539697006453
Test Mean absolute error : 1.8273355773850983]

## 🚀 How to Run Locally
1. Clone the repo:
```bash
   git clone https://github.com/12102004-Tapas/House-Price-Prediction.git
   cd House-Price-Prediction
```
2. Install dependencies:
```bash
   pip install streamlit pandas numpy scikit-learn xgboost
```
3. Run the app:
```bash
   streamlit run app.py
```

## 📁 Files
- `app.py` — Streamlit app code
- `house_price_model.pkl` — Trained XGBoost model
- `housing.csv` — Training dataset

## 👤 Author
Tapas Mahapatra — MCA Student, Data Science & Analytics
