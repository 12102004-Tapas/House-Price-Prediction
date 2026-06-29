import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))

st.title('🏠 House Price Prediction App')

# Input fields
CRIM = st.slider('Crime Rate (CRIM)', 0.0, 100.0, 0.00632)
ZN = st.slider('Residential Land Zone (ZN)', 0.0, 100.0, 18.0)
INDUS = st.slider('Industrial Area (INDUS)', 0.0, 30.0, 2.31)
CHAS = st.selectbox('Near River? (CHAS)', [0, 1])
NOX = st.slider('Nitric Oxide (NOX)', 0.0, 1.0, 0.538)
RM = st.slider('Avg Rooms (RM)', 1.0, 10.0, 6.575)
AGE = st.slider('Age of House (AGE)', 0.0, 100.0, 65.2)
DIS = st.slider('Distance to Employment (DIS)', 0.0, 15.0, 4.09)
RAD = st.slider('Highway Access (RAD)', 1, 24, 1)
TAX = st.slider('Tax Rate (TAX)', 0.0, 800.0, 296.0)
PTRATIO = st.slider('Pupil Teacher Ratio (PTRATIO)', 0.0, 25.0, 15.3)
B = st.slider('Black Population Index (B)', 0.0, 400.0, 396.9)
LSTAT = st.slider('Lower Income Population % (LSTAT)', 0.0, 40.0, 4.98)

# Predict button
if st.button('Predict Price'):
    input_data = pd.DataFrame([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]],
                    columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT'])
    
    predicted_price = model.predict(input_data)
    st.success(f'🏠 Predicted House Price : ${predicted_price[0]*1000:,.2f}')