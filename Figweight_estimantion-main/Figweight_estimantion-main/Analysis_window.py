import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from PIL import  Image
import time
from plotly.offline import iplot

def app():
    header = st.container()
    nav = st.container()
    add = st.container()
    vis = st.container()

    with header:
        # main_logo_path = r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\images (1).jfif'
        main_logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\EUHjAbGX0AEIhku.jfif'
        main_logo = Image.open(main_logo_path).resize((800, 400))
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.image(main_logo)
        # with col2:
        #     st.image(main_logo)
        # with col3:
        #     st.image(main_logo)
        # col1 = st.columns(1)
        # with col1:
        st.image(main_logo)
        # with col2:
        #     st.image(main_logo)
        # with col3:
        #     st.image(main_logo)
        st.title('Pig Weight Management')

        # st.write("<Project title:> Development of AI for measuring animal volume and weight based on images.")
        st.markdown("**Project title:** Development of AI for measuring animal volume and weight based on images.")

        st.markdown("**Description:** Collection and processing of volume data for pig. Calculation of the volume of the subject captured by a camera without the need for scale.")
        st.markdown("**Input:** Images.")
        st.markdown("**Ouptut:** Weight of pigs.")

        st.title('DATA ANALYSIS')
        st.write("Briefly explain how to do this project.")

        st.write("""
            1 - Labeling images with two classes: Pig and pads as the metric to convert pixels to size.
                    
                a) Pig   
                b) Pads 
            2 - How to convert from pixel to size.
                    
                Real pads size 50x70: -> area = 3500 unit
                Example: volumes area of the pad = 350 pixels (result of segmentation task)
                """    
                # <strong>1 pixels equal to <span style='color:red'> 35 unit</span></strong>
                
            )
        st.markdown(" As the result:    **1 pixels equal to 10 unit**.")
        st.markdown("**Example:** Output of model are 140 pixels for length and 50 for heart girth")
        st.markdown("this time we will convert from pixels to size.")
        st.markdown("From 140 pixels to 140*10 = 1400")
        st.markdown("From 50 pixels to 50*10=500") 
        # st.latex('Weight = \dfrac{Girth^2 * Length}*{69.3} = \dfrac{1.4^2 * 0.5}{69.3} = ')
        st.latex('Weight = Girth^2 * Length*69.3')

        st.image(Image.open(r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\labels.png'))


    with nav:

        # logo_path = r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\images.jfif'
        logo_path = r'D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\Figweight_estimantion-main\Figweight_estimantion-main\img\Screenshot 2024-04-02 165524.png' #anh quan ly heo
        # (.jfif)
        logo = Image.open(logo_path)
        resize_logo = logo.resize((180, 100))
        st.sidebar.image(resize_logo)

        st.sidebar.write('Select visualization method:')

        vis_sub = st.sidebar.checkbox('Sample Pig images by subspecices')

        subspec = st.sidebar.checkbox('Subspecies distribution') # amount of images in this project

        health_dis = st.sidebar.checkbox('Apply data agumentation')


        img_loca_heal_sub = st.sidebar.checkbox('Features map')


    with vis:
        if vis_sub:
            st.write('Data visualization')

            st.write('A sample of fresh fish')
            st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\New folder\Classification task\KakaoTalk_20221004_094236830_18.jpg'))
            
            st.write('A sample of infected fish')
            st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\New folder\Classification task\KakaoTalk_20221004_133311545_25.jpg'))

            
        if subspec:
            st.image(Image.open(r'/home/nghia/Downloads/Bee/subspecies.png'))
        
        if health_dis:
            st.write("An example of data agumentation technique")
            st.write("-----------------------------------------")
            st.write("The orginal image")
            st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\fish.jpg'))
            

       
        if img_loca_heal_sub:
            st.write("The orginal image")
            st.image(Image.open(r'C:\Users\NgocHuynh\Downloads\fishhealth-main\fishhealth-main\img\New folder\Classification task\KakaoTalk_20221004_094236830_13.jpg'))
            st.write("-----------------------------------------")
            st.write("Visualize feature maps")

            st.image(Image.open(r'D:\New Volume(D old)\Master Course\Semester 03\Advanced Project for AI convergence\feature maps.png'))

   
