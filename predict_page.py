# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:27:59 2022


"""
import streamlit as st
import pickle
import numpy as np
from PIL import Image

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model()

regressor = data["model"]


def show_predict_page():
    st.title("Tijuana House Prices Predictor")
    
    st.write("""### Find out how much a house in Tijuana costs based on certain features!""")
    image = Image.open('Zona_Rio_Tijuana.jpg')
    st.image(image, caption = 'Zona Rio is one of the most popular areas of Tijuana')
   
    bedroom = st.slider("Number of bedrooms", 1,10)
    bathroom = st.slider("Number of bathrooms", 1, 4)
    parking = st.slider("Number of parking spots", 1, 4)
    size = st.slider("Property size (in square feet)", 75, 1000, step = 25)
    distance_SY = st.slider("Distance to San Ysidro border (in kilometers)", 5.0, 25.0, step = 0.5)
    distance_OT = st.slider("Distance to Otay border (in kilometers)", 5.0, 25.0, step = 0.5)
    
    ok = st.button("Calculate house price")
    if ok:
        x = np.array([[bedroom, bathroom, parking, size, distance_SY, distance_OT]])
        x = x.astype(float)
        
        price = regressor.predict(x)
        st.subheader(f"The estimated house price is ${price[0]:,.2f}")



    