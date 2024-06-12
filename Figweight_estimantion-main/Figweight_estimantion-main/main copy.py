import streamlit as st
import pandas as pd
from PIL import  Image
import Train_window
import Predict_window
import Analysis_window

PAGES = {
    "Data analysis stage": Analysis_window,
    "Training stage": Train_window,
    "Prediction stage": Predict_window
}

logo_path = r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\images.jfif'
# logo_path = r'C:\Users\NgocHuynh\Downloads\MYBOX\images\infection\20220929_194608.jpg'
logo = Image.open(logo_path)
resize_logo = logo.resize((180,100))
st.sidebar.image(resize_logo)
st.sidebar.title('STAGE')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()