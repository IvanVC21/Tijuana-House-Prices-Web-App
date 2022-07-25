import streamlit as st
from PIL import Image

def show_about_page():
    st.title("Welcome to Tijuana House Prices Web App!")
    image = Image.open('cecut.jpg')
    st.image(image, caption = 'Going to Tijuana Cultural Center (CECUT) is always a great idea.')
    
    st.write("Hi my name is Ivan Verdugo and I present to you the Tijuana House Prices Web App.")
    st.write("The main purpose of this project is to have a predictor that gives us a house price given certain features. It was made by web scraping the website [Inmuebles24](https://www.inmuebles24.com/) and developed in Python. Huge shoutout and acknowledgement to one of my best friends and colleague [Jesus Hector Zamora](https://www.linkedin.com/in/jesus-hector-zamora/), as he helped me with the web scrapping and getting the coordinates for every house!")
    
    st.write("""### Big Takeaways""")
    st.write("* Initially we had 888 houses but after getting rid of null rows and houses that didn't specify the address we were left with 576 houses.")
    st.write("* In order to get rid of outliers, we used above 95 percentile as the max threshold and below 5 percentile as lowest threshold. After getting rid of outliers, we were left with 517 houses.")
    st.write("* Most important feature for calculating price was the number of bathrooms with 0.56 Pearson Correlation Score.")
    st.write("* 9 regression models were used for this project being XGBoost Regressor the model with best performance on test data with 0.77 R2 score, which is the model that we can use in the Predict page.")
    st.write("* The plots shown on the Explore page are made with outliers except the Price for location plot.")
    
    st.write("""### Considerations for further versions""")
    st.write("* As with any data project, the more data that we have the better. Surely, with more than 517 houses we could build better models.")
    st.write("* We missed a better way to sectorialize the houses. A cluster was made in order to classify the houses as West, Mid-West, Mid-East and East but once they were included in the models they failed to improve these.")
    st.write("* Having more features like the materials of which the house is made or the time since the house was built could significantly improve the models.")
    st.write("* An Artificial Neural Network was implemented, however in didn't gave a better performance than previous models. As I'm currently studying TensorFlow and Deep Learning, in the future we could retry this ANN approach, however in the case still we don't get better results it won't be a surprise because [tree-based models are still better than neural nets when working with tabular data.](https://arxiv.org/abs/2207.08815)")
    
    
    st.write("I learned a lot and had some fun doing this project. Hope to look it again in the future with more knowledge in order to improve it. Thank you for reading this far and have fun using this app.")
    st.write("I'm always open to hear feedback and I would deeply appreciate it! You can contact me through [LinkedIn](https://www.linkedin.com/in/ivanverdugo-analytics/) or you can shoot me an email to jesusivan.vc21@gmail.com")
    st.write("You can see the full code required to do this app in its [GitHub repo.](https://github.com/IvanVC21/Tijuana-House-Prices)")
