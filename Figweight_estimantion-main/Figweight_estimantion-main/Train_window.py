import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from PIL import  Image
import time
from plotly.offline import iplot

import numpy as np
import cv2 


foler = r'D:/New Volume(D old)/PhD Course/Courses/Second semester/AI project/Fig - AI project code/Figweight_estimantion-main/Figweight_estimantion-main/img/'
def app():
    header = st.container()
    model = st.container()
    add = st.container()
    train = st.container()
# D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\Screenshot 2024-04-02 164011.png
    with header:
        main_logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\Screenshot 2024-04-02 164011.png'
        # main_logo_path = r'C:\Users\NgocHuynh\Downloads\MYBOX\images\infection\20220929_194608.jpg'

        main_logo = Image.open(main_logo_path).resize((800, 400))
        st.image(main_logo)
        st.title('Fish Health Management')
        st.title('TRAINING')

    col1, col2 = st.columns(2)
    with col1:
        train_progress = st.button('Train')
    with col2:
        cancel = st.button('Cancel')
    #with col3:
     #   jump = st.button('Go to prediction window')

    if train_progress:
        my_bar = st.progress(0)
        for percent in range(100):
            time.sleep(1.2)
            my_bar.progress(percent + 1)

        #with st.spinner('Training'):
        #    time.sleep(3)
        st.success('Done!')

    with model:
        logo_path = r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\images.jfif'
        logo = Image.open(logo_path)
        resize_logo = logo.resize((180,100))
        st.sidebar.image(resize_logo)
        st.sidebar.selectbox('Select your training model:',
                             ('Detectron2 - Segmentation task', 'CNN - Classification task'))
        thresh = st.sidebar.slider('Select your threshold:', 0.0, 1.0, 0.1)

    with add:
        # file = st.file_uploader('Upload your image')
            image_files = st.file_uploader('Upload your image', accept_multiple_files=True)
            label_files = st.file_uploader('Upload your labels', accept_multiple_files=True)
            # Display the uploaded files
             # Flag to track if both uploads have occurred
            # uploads_complete = image_files is not None and label_files is not None
            uploads_complete = image_files and label_files
# Display the uploaded files
            if image_files:
                st.write("Uploaded Images")
                # for img in image_files:
                #     st.image(Image.open(img))

            if label_files:
                st.write("Uploaded Labels")
                # for label in label_files:
                #     # st.write(label.read().decode('utf-8'))
                #     st.image(Image.open(img))

                    # Display example image after processing uploads
            # print('ac')
            if uploads_complete:
                # time.sleep(5)  # Add a delay to simulate processing time
                st.write("Example image of training set")
                st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\input.png'))
            # print('ac')
            # if image_files:
            #     st.write("Uploaded Images")
            #     for img in image_files:
            #         st.image(img)
            
            # if label_files:
            #     st.write("Uploaded labels")
            #     for img in label_files:
            #         st.image(img)
    
            # if label_files:
            #     handle_file_upload(label_files, 'label')
            # st.write('s', file)
            # st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\predict\predict 1_use.png'))
            # time.sleep(5)
            # st.write("Example image of traning set")
            # if uploads_complete:
            #     time.sleep(5)  # Add a delay to simulate processing time
            #     st.write("Example image of training set")
                # st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\input.png'))

            
            # st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\input.png'))
            
            
            
            # st.image(Image.open(foler + 'input.png'))



    # with add:
    #     uploaded_files = st.file_uploader('Upload your image', accept_multiple_files=True)
    
    #     if uploaded_files is not None:
    #         for uploaded_file in uploaded_files:
    #             file_bytes = uploaded_file.read()
    #             st.image(file_bytes, caption='Uploaded Image.', use_column_width=True)



    with train:
        ratio = st.slider('Select training ratio (%):')
        st.write('training rate is ', ratio,'%')
        st.write('toal training images', ratio*3)

    # with test:
    #     st.
    if cancel:
        st.write('Cancel training!')
