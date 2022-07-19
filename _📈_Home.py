import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
image = Image.open('data/img_1_4.jpg')

st.set_page_config(page_title='Oil price Forecasting', page_icon='📈', layout="centered", initial_sidebar_state="expanded", menu_items=None)
#
st.cache()
df = pd.read_excel('data/RBRTE Data.xlsx')

st.title("Forecasting Crude oil prices...")
st.markdown('---')
st.image(image)
st.markdown('---')


date=st.sidebar.date_input("Enter the date till you want you forecast.")

