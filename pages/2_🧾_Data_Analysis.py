import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from helper import data_preprocessor

st.cache()
df = data_preprocessor('data/RBRTEd.xls') # month extraction



st.set_page_config(page_title='Data_Analysis', page_icon='💨', layout="centered", initial_sidebar_state="expanded", menu_items=None)
st.title("Data Analysis...")
st.markdown("---")
st.header("Oil price Data")
st.dataframe(df)
st.markdown("---")
st.header("Line Chart. ")
fig = px.line(data_frame=df,x='Date',y='Price',title="Crude Oil Prices over the years.",
              color_discrete_sequence=['#810955'])
fig.update_layout(
    autosize=True,
    width=750,
    height=400,
    margin=dict(
        l=5,
        r=10,
        b=15,
        t=50,
        pad=4),
    xaxis=dict(showgrid=False),   #disabling grids
    yaxis=dict(showgrid=False),
    plot_bgcolor='#f5e1e1',       #setting bgcolor
    paper_bgcolor="#FAF2F2",      #setting plotbg color
    title_x=0.3,                  #adjusting title
    title_font=dict(              #working with font
            family="Helvetica",
            size=20,
            color='#810955'
        ))
fig.update_xaxes(color='#810955') #alterations on xaxes
fig.update_yaxes(color='#810955') #alterations on yaxes
st.plotly_chart(fig)

st.markdown('---')
st.header('Boxplots..')
fig = px.box(data_frame=df,x='Years',y='Price',title="Boxplots of Each year.",
              color_discrete_sequence=['#810955'])
fig.update_layout(plot_bgcolor='#F1FFF1',
                  paper_bgcolor='#C4F0C5',
                  title_x=0.3,                  #adjusting title
                  title_font=dict(              #working with font
                family="Helvetica",
                size=20,
                color='#810955'
        ))
fig.update_xaxes(rangeslider_visible=True)
fig.update_xaxes(color='#810955')
fig.update_yaxes(color='#810955')
st.plotly_chart(fig)

fig = px.box(data_frame=df,x='Months',y='Price',title="Boxplots of Each Month.",
              color_discrete_sequence=['#233714'])
fig.update_layout(plot_bgcolor='#F1FFF1',
                  paper_bgcolor='#C4F0C5',title_x=0.3,                  #adjusting title
                  title_font=dict(              #working with font
                family="Helvetica",
                size=20,
                color='#810955'
        ))
fig.update_xaxes(color='#810955')
fig.update_yaxes(color='#810955')
st.plotly_chart(fig)
st.markdown('---')

st.title("Histograms..")
fig=px.bar(data_frame=df.groupby(by='Years')['Price'].mean(),title="Average crude oil Prices for Each year",
              color_discrete_sequence=['#5FD068'])
fig.update_xaxes(tickangle=270)
fig.update_xaxes(color='#5FD068')
fig.update_yaxes(color='#5FD068')
fig.update_layout(title_x=0.2,                  #adjusting title
                  title_font=dict(              #working with font
                family="Helvetica",
                size=20,
                color='#810955'
        ))
st.plotly_chart(fig)


fig=px.bar(data_frame=df.groupby(by='Months')['Price'].mean(),title="Average crude oil Prices for Each Month",
              color_discrete_sequence=['#5FD068'])
fig.update_xaxes(tickangle=270)
fig.update_xaxes(color='#5FD068')
fig.update_yaxes(color='#5FD068')
fig.update_layout(title_x=0.2,                  #adjusting title
                  title_font=dict(              #working with font
                family="Helvetica",
                size=20,
                color='#810955'
        ))
st.plotly_chart(fig)


st.markdown('---')
st.header("Heatmap..")
fig= px.density_heatmap(df,x='Years',y='Months',z='Price',histfunc='avg',template='seaborn',
                        text_auto=False,title="Detailed Heatmap with Range selector")
fig.update_layout(height=600,width=700  ,plot_bgcolor='#FFDEDE')
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_x=0.2,                  #adjusting title
                  title_font=dict(              #working with font
                family="Helvetica",
                size=20,
                color='#810955'
        ))
st.plotly_chart(fig)
st.markdown('---')

