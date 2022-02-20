import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import plotly.express as px
import base64
from PIL import Image
life = pd.read_csv("https://raw.githubusercontent.com/MohannadRif42/StreamlitMAR42/main/LifeEx1.csv")
covid = pd.read_csv("https://raw.githubusercontent.com/MohannadRif42/StreamlitMAR42/main/covid19.csv")

def get_base64_of_bin_file(bin_file):
    """
    function to read png file
    ----------
    bin_file: png -> the background image in local folder
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://unblast.com/wp-content/uploads/2021/01/Space-Background-Image-2.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()


var1 = st.sidebar.radio("What do you want to View",["General Info","Covid19 Scatter Plot","Life Expectancy Scatter Plot","Animated Scatter Plot LifeEX","Life Expectancy Animated Map","LifeEx 3D Scatter Plot"])

if var1 == "General Info":

    image1 = "https://www.deccanherald.com/sites/dh/files/articleimages/2020/12/17/covid-19-49829101920-928209-1608156401.jpg"
    st.header("What Is Coronavirus?")
    st.image(image1,width=430)
    st.write("""Coronaviruses are a type of virus. There are many different kinds, and some cause disease. A coronavirus identified in 2019, SARS-CoV-2, has caused a pandemic of respiratory illness, called COVID-19.""")
    st.header("How did the coronavirus start?")
    st.write("""The first case of COVID-19 was reported Dec. 1, 2019, and the cause was a then-new coronavirus later named SARS-CoV-2. SARS-CoV-2 may have originated in an animal and changed (mutated) so it could cause illness in humans. In the past, several infectious disease outbreaks have been traced to viruses originating in birds, pigs, bats and other animals that mutated to become dangerous to humans. Research continues, and more study may reveal how and why the coronavirus evolved to cause pandemic disease.""")
    st.header("How does the coronavirus spread?")
    st.write("""As of now, researchers know that the coronavirus is spread through droplets and virus particles released into the air when an infected person breathes, talks, laughs, sings, coughs or sneezes. Larger droplets may fall to the ground in a few seconds, but tiny infectious particles can linger in the air and accumulate in indoor places, especially where many people are gathered and there is poor ventilation. This is why mask-wearing, hand hygiene and physical distancing are essential to preventing COVID-19.""")
    st.header("How do you protect yourself from this coronavirus?")
    st.write("""Vaccines are now authorized to prevent infection with SARS-CoV-2, the coronavirus that causes COVID-19. But until more is understood about how the vaccines affect a person’s ability to transmit the virus, precautions such as mask-wearing, physical distancing and hand hygiene should continue regardless of a person’s vaccination status to help prevent the spread of COVID-19. Learn more about the COVID-19 vaccine and ways to protect yourself.""")

covid["ObservationDate"] = pd.to_datetime(covid["ObservationDate"])
startdate = '2020-01-22'
enddate = '2020-05-1'
mask = (covid['ObservationDate'] > startdate) & (covid['ObservationDate'] <= enddate)
covid = covid.loc[mask]
if var1 == "Covid19 Scatter Plot":
    st.header("Covid19 Scatter Plot")
    st.write("""This graph represent the relationship between the confirmed covid_19 cases and the death covid_19 cases for each country around the world in specific period of time.
""")
    fig1, ax = plt.subplots()
    ax4 = px.scatter(covid,x="Confirmed",y="Deaths",color="Country/Region",size ="Recovered",size_max=30)
    st.write(ax4)


life = life.dropna()
if var1 == "Life Expectancy Scatter Plot":
    st.header("Life Expectancy Scatter Plot")
    st.write("""This graph represent the relationship between the Alcohol and the Life Expectancy for each country around the world from 2000 till 2015.
""")
    fig, ax = plt.subplots()
    ax = px.scatter(life,x="Alcohol",y="LifeEx ",color="Country",size ="Year",size_max=10)
    st.write(ax)

if var1 == "Animated Scatter plot LifeEX":
    st.header("Animated Scatter plot LifeEX")
    st.write("""This graph shows animated Scattter plot for life expectancy""")
    ax1 = px.scatter(life,x="LifeEx ",y="Adult_Mortality",color="Country",animation_frame="Year",size="Alcohol",size_max=90,animation_group="Country",log_x=True,range_x=[10,100],range_y=[1,800])
    st.write(ax1)

if var1 == "Life Expectancy Animated Map":
    st.header("Life Expectancy Animated Map")
    st.write("""This animated map shows how the Life Expectancy rate changes around the world from 2000 till 2015
""")
    ax2= px.choropleth(life,locations="Country",locationmode="country names",color="LifeEx ",animation_frame="Year",color_continuous_scale=px.colors.sequential.Plasma)
    st.write(ax2)


startdate2 = 2010
enddate2 = 2012
mask1 = (life['Year'] > startdate2) & (life['Year'] <= enddate2)
life2 = life.loc[mask1]

if var1 == "LifeEx 3D Scatter Plot":
    st.header("LifeEx 3D Scatter Plot")
    st.write("""This 3D scatter plot shows the relationship between the Life Expectancy and Adult Mortality for every country arounf the world.
""")
    ax3 = px.scatter_3d(life2, x='LifeEx ', y='LifeEx ',z='Adult_Mortality',color="Country")
    st.write(ax3)
