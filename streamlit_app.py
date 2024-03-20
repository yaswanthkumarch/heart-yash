from typing import Any 
import streamlit as st
import pandas as pd 

import pickle
import time
from PIL import Image
st.set_page_config(page_title="Final Project", layout="wide")

# Center-aligned text using CSS
st.markdown("""
    <h1 style='text-align: center;'>Welcome to Heart Disease Machine Learning Dashboard</h1>
    """, unsafe_allow_html=True)
options = ("Option 1", "Option 2", "Option 3")
selected_option = st.sidebar.selectbox("Select an option", options, index=0)
#buat logo heart disease ke tengah
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image('niceheart.jpg', width=350)

with col3:
    st.write(' ')
st.write("""
    Heart disease refers to a group of conditions that can affect the heart's functioning. This includes coronary artery disease, heart failure, arrhythmias, and many other conditions. Heart disease can be life-threatening and is often associated with risk factors such as high blood pressure, high cholesterol levels, poor dietary habits, smoking, lack of physical activity, and genetic factors. 
    """)

st.write("""
- Age (Patient's Age): This variable records the age of the patient in years. Age can be a significant risk factor in the development of heart disease, as the risk of heart disease tends to increase with advancing age.

- Sex (Gender): This variable indicates the gender of the patient, with a value of 1 for male and 0 for female. Some studies suggest that the risk of heart disease may differ between males and females, with males often having a higher risk.

- CP (Chest Pain Type): This variable describes the type of chest pain experienced by the patient. It has four category values:
Value 1: Typical Angina (Stable Angina)
Value 2: Atypical Angina (Unstable Angina)
Value 3: Non-Anginal Pain
Value 4: Asymptomatic (Without Symptoms)
Chest pain is a common symptom that can be an indicator of heart problems.

- Thalach (Maximum Heart Rate): This is the maximum heart rate of the patient. A high maximum heart rate can indicate good heart performance.

- Exang (Exercise-Induced Angina): This is a binary variable indicating whether the patient experiences angina during exercise. A value of 1 indicates the presence of angina, while 0 indicates the absence of angina.

- Oldpeak (ST Depression): ST depression is a change on an electrocardiogram (EKG) that occurs during a stress test relative to rest. This variable measures the extent of ST depression.

- Slope: This is a variable that describes the slope of the EKG segment during a stress test. It can have three values: 0 (downsloping), 1 (flat), and 2 (upsloping).

- CA (Number of Major Vessels): This is the number of major blood vessels with significant narrowing (0-3). The number of narrowed blood vessels can be an indicator of coronary heart disease.

- Thal (Thallium Scan Result): This variable represents the result of a thallium scan test with three categories: 1 (normal), 2 (fixed defect), and 3 (reversible defect).
""")
