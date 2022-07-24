import streamlit as st
from PIL import Image

def show_about_page():
    st.title("Welcome to Tijuana House Prices Web App!")
    image = Image.open('cecut.jpg')
    st.image(image, caption = 'Going to Tijuana Cultural Center (CECUT) is always a great idea.')
    
    st.write("Hi my name is Ivan Verdugo and I present to you the Tijuana House Prices Web App.")
    st.write("It was made by web scraping the website [Inmuebles24](https://www.inmuebles24.com/) and developed in Python. Huge shoutout and acknowledgement to one of my best friends and colleague [Jesus Hector Zamora](https://www.linkedin.com/in/jesus-hector-zamora/), as he helped me with the web scrapping and getting the coordinates for every house!")
    
    st.write("""### Big Takeaways""")
    st.write("* Initially we had 888 houses but after getting rid of null rows and houses dand didn't specify the address we were left with 576 houses.")
    st.write("* In order to get rid of outliers, we used above 95 percetile as the max threshold and below 5 percentile as lowest threshold. After getting rid of outliers, we were left with 517 houses.")
    st.write("* Most important feature for calculating pricen was the number of bathrooms with 0.56 Pearson Correlation Score.")
    st.write("* 6 regression models were used for this project being xGBoost Regressor the model with best performance on test data with 0.77 R2 score.")
    
    st.write("""### Considerations for further versions""")
    st.write("* As with any data project, the more data that we have the better. Surely, with more than 517 houses we could build better models.")
    st.write("* We missed a better way to sectorialize the houses. A cluster was made in order to classify the houses as West, Mid-West, Mid-East and East but once they were included in the models they failed to improve these.")
    st.write("* Having more features like the materials of which the house is made or the time since the house was built could significantly improve the models.")
    
    
    st.write("I learned a lot and had some fun doing this project. Hope to look it again in the future with more knowledge in order to improve it. Thank you for reading this far and have fun using this app.")
    st.write("Im always open to hear feedback and I would deeply appreciate it! You can contact me through [LinkedIn](https://www.linkedin.com/in/ivanverdugo-analytics/) or you can shoot me an email to jesusivan.vc21@gmail.com")
    