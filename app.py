import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from about_page import show_about_page
page = st.sidebar.selectbox("What would you like to do?", ("Learn about the project", "Predict", "Explore"))
if page == "Learn about the project":
    show_about_page()
elif page == "Predict":
    show_predict_page()
else:
    show_explore_page()




