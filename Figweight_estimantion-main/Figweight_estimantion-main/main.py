import streamlit as st
import pandas as pd
from PIL import  Image
import Train_window
import Predict_window
import Analysis_window
# D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\fish.jpg
PAGES = {
    "Project description": Analysis_window,
    "Training stage": Train_window,
    "Prediction stage": Predict_window
}

# logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\EUHjAbGX0AEIhku.jfif'
logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\Screenshot 2024-04-02 164011.png'
logo = Image.open(logo_path)
resize_logo = logo.resize((180,100))
st.sidebar.image(resize_logo)
st.sidebar.title('STAGE')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()