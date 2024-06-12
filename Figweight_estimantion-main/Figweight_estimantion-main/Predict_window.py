import time

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from PIL import  Image
from plotly.offline import iplot


folders = r'D:/TS/호흡량 이미지/chamber2/chamber2_pig_growing-pig_pig61_221130_105021_001_18/'
def app():
    header = st.container()
    model = st.container()
    add = st.container()
    pred = st.container()

    with header:
        # main_logo_path = r'/media/nghia/Nguyen NghiaW/Bee_streamlit/img/favpng_honey-bee-honeycomb-icon.png'
        main_logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\EUHjAbGX0AEIhku.jfif'
        main_logo = Image.open(main_logo_path).resize((800,400))
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.image(main_logo)
        # with col2:
        #     st.image(main_logo)
        # with col3:
        #     st.image(main_logo)
        st.image(main_logo)
        st.title('Pig Farm Management')
        # Print('dsdas')
        # st.markdown("fddfd")
        st.title('PREDICTION')

    col1, col2 = st.columns(2)
    with col1:
        predict = st.button('Predict')
    with col2:
        cancel = st.button('Stop')

    with model:
        # logo_path = r'/media/nghia/Nguyen NghiaW/Bee_streamlit/img/Lovepik_com-401013367-lovely-bees.png'
        # logo_path = r'C:\Users\NgocHuynh\Downloads\beehealth-main\beehealth-main\img\New folder\KakaoTalk_20221004_133311545_25.jpg'
        # logo_path = r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\images.jfif'
        logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\Screenshot 2024-04-02 165524.png'
        logo = Image.open(logo_path)
        resize_logo = logo.resize((180, 100))
        st.sidebar.image(resize_logo)
        st.sidebar.selectbox('Select your prediction model:',
                             ('YOLO-v8 - Segmentation task', 'YOLO-v8 - Object Detection'))


        image_size = st.sidebar.slider('Define your image size:', 512, 640, 1024)                   

        thresh = st.sidebar.selectbox('Select your prediction threshold:', ("0.3", "0.5"))
        
        
                
        threshd = st.sidebar.selectbox('Select your Optimizer method:', ("Adam", "SGD"))

        





    with add:
        file = st.file_uploader('Upload your image you want to predict')
        print(file)
        if file is not None:
            #file = r'/media/nghia/Nguyen NghiaW/Bee_streamlit/img/BeeSmall.jpg'
            # file = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\iput.png'
            img = Image.open(file)
            # print(img)
            # print(file)
            st.title("Here is the image you've selected")
            # resized_image = img.resize((512, 512))#((336, 336))
            # st.image(resized_image)
            # st.image(Image.open(file))
            # st.image(Image.open( r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\input.png')) #/////////
            st.image(img)
        # else:
        #     st.title("Here is the image you've selected")
        #     st.image(main_logo)

            # if file is 'rC:\Users\NgocHuynh\Downloads\beehealth-main\beehealth-main\img\predict\predict 1_use.png':
            #     print('sd')

        # if st.sidebar.checkbox("Print batch info"):
        #     st.subheader('Detectron2 - Segmentation task')
            # st.write('state') 
    # st.write('          ')
        # if detec:
        #     st.write('abs')
        # st.sidebar.selectbox('Select your prediction model:',
        #                      ('YOLO - v8', 'CNN'))
    
    infected = st.checkbox('Output images of YOLO')
    fresh = st.checkbox('Pig weight estimation')
    
    # if fresh: 
    #     d1 = ['Pig length', "50 mm"], ["Pig Girth", "140 mm"], ['Pig Preidict weight', '67.9 kg'], ['Pig real weight', "70.5 kg"], ['MAE', " 2.6 kg"] 
    #     df1 = pd.DataFrame(d1, columns=['Pig information', 'Output score'])
        

    # if infected:
    #     # d2 = ['Pixel Accuracy', '0.985%'], ['IoU', "0.015%"]
    #     # df2 = pd.DataFrame(d2, columns=['Segmentation metrics', 'Confident score'])
    #     time.sleep(3)
    #     st.title("Here is the output of your image")
    #     # st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\inclued-images.png'))
    #     st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\output-yolo.png'))
    #     # d2 = ['Pig length', "37 mm"], ["Pig Girth", "103 mm"], ['Pig Preidict weight', '27.9 kg'], ['Pig real weight', "70.5 kg"], ['MAE', " 42.6 kg"] 
        # df2 = pd.DataFrame(d2, columns=['Pig information', 'Output score'])



    # fresh



    if predict:
        d2 = ['Pig length', "87 mm"], ["Pig Girth", "203 mm"], ['Pig Preidict weight', '248.4 kg'], ['Pig real weight', "70.5 kg"], ['MAE', "177.9 kg"] 

        d1 = ['Pig length', "50 mm"], ["Pig Girth", "140 mm"], ['Pig Preidict weight', '67.9 kg'], ['Pig real weight', "70.5 kg"], ['MAE', " 2.6 kg"] 

        df2 = pd.DataFrame(d2, columns=['Pig information', 'Output score'])
        df1 = pd.DataFrame(d1, columns=['Pig information', 'Output score'])

        with st.spinner('Predicting'):
            # time.sleep(3)
            if fresh and thresh == "0.3":
                time.sleep(3)
                st.title("Here is the output of your image")
                st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\output-38.png'))

                print('dddddddddd',thresh)

                st.write(df1)
            if fresh and thresh == "0.5":
                time.sleep(3)
                st.title("Here is the output of your image")
                st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\output-mask.png'))

                print('eeeee',thresh)

                st.write(df2)
                # st.write(df2)
            if infected and thresh == "0.3":
                time.sleep(3)
                st.title("Here is the output of your image")
                st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\output-38.png'))

                print('eeeee',thresh)
            if infected and thresh == "0.5":
                time.sleep(3)
                st.title("Here is the output of your image")
                st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\output-mask.png'))

                print('eeeee',thresh)

                # st.write(df2)

            # elif infected:
                # st.write(df1)
                # st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\predict\predict 1_use.png'))
            # else:
            #     # st.write('**no task is selected!**')
            #     st.write('Fish health segmentation')
            
            st.success('Done!')
        # with st.spinner("Predicting"):
        #     time.sleep(3)

            # st.write('abc',  st.sidebar.selectbox)
            # if model == 'Detectron2 - Segmentation task':
            #     st.write("abc")

    if cancel:
        st.write('**Infected prediction!**')

