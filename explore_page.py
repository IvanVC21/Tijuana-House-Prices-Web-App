import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/IvanVC21/Tijuana-House-Prices/main/EDA.csv'
    df = pd.read_csv(url)
    
    return df


df = load_data()

def show_explore_page():
    st.title("Explore Tijuana House Prices data")
    
    st.write(
        """
    ### Dive in the visualizations in order to have a better understanding of the data!
    """
    )
    image = Image.open('revu.jpg')
    st.image(image, caption = 'Worldwide famous Avenida Revolucion is a tourist center known for its endless nightlife options.')
    
    dist = sns.displot(df.price, aspect = 2, height = 3)
    dist.set(xlabel = "Price (Millions of USD)", ylabel = "Number of houses")
    
    st.write("""#### Distribution of house prices""")
    st.pyplot(dist)
    
    
    corr, ax = plt.subplots()
    sns.heatmap(df.corr(), cmap = 'coolwarm', annot = True)
    
    st.write("""#### Correlations between variables""")
    st.pyplot(corr)
    
        
    loc = sns.catplot(x= 'location', kind="count", palette="ch:.25", height = 4, aspect = 1, data=df)
    loc.set(xlabel= "Zones of the city", ylabel = "Number of houses")
    st.write("""#### Count of houses by location""")
    st.pyplot(loc)
    
    
    box = plt.figure(figsize=(10, 4))
    ax = sns.boxenplot(x="location", y="price", data=df, showfliers=(False))
    ax.set(xlabel="Zones of the city", ylabel = "Price (Millions of USD)")
    st.write("""### Price by location""")
    st.pyplot(box)
    
    
    

