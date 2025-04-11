import streamlit as st
import requests
import tempfile
import os
import time
from io import BytesIO
import subprocess
import atexit


url = "http://13.229.206.194:8502/api/v1/predict/"
headers = {
  'Content-Type': 'application/json'
}

st.title("ML Model Servering Over REST API")

text = st.text_area("Enter text to analyze sentiment:")
data = {
  "text": text
}
if st.button("Predict"):
    with st.spinner("Predicting... Please Wait!!!"):
        response =requests.post(url, headers=headers, json=data)
        output = response.json()
    st.write(output['label'])

#python -m streamlit run streamlit_app.py --server.enableXsrProtection false