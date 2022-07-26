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




# """Data Preprocessing"""
df['Date']= pd.to_datetime(df['Date'],utc=False)
df['Price']= pd.to_numeric(df['Price'])
df.set_index(df['Date'])
y = df['Price'].fillna(method='ffill')
y = y.values.reshape(-1, 1)

# scale the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0, 1))
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(y)
y = scaler.transform(y)

n_lookback = 90
n_forecast = 90

X = []
Y = []
for i in range(n_lookback, len(y) - n_forecast + 1):
    X.append(y[i - n_lookback: i])  #90 - 90 : 90
    Y.append(y[i: i + n_forecast])  #90 : 90+90

X = np.array(X)
Y = np.array(Y)

X_ = Y[-n_lookback:len(y)]  # last available input sequence

from tensorflow import keras
model = keras.models.load_model('Models/lstm_1.h5')

Y_ = model.predict(X_).reshape(-1, 1)
Y_ = scaler.inverse_transform(Y_)

df_past = df
df_past=df_past.set_index(df_past['Date'])
df_past.rename(columns={'index': 'Date', 'Price': 'Actual'}, inplace=True)
df_past['Date'] = pd.to_datetime(df_past['Date'])
df_past['Forecast'] = np.nan
df_past['Forecast'].iloc[-1] = df_past['Actual'].iloc[-1]

df_future = pd.DataFrame(columns=['Date', 'Actual', 'Forecast'])
df_future['Date'] = pd.date_range(start=df_past['Date'].iloc[-1] + pd.Timedelta(days=1), periods=n_forecast)
df_future['Forecast'] = Y_.flatten()
df_future['Actual'] = np.nan

results = df_past.append(df_future).set_index('Date')
date=st.sidebar.date_input("Enter the date till you want you forecast.")
final = results.loc['1987-05-20': date]

st.header("Crude Oil Prices [Forecasted]")
fig = px.line(data_frame=final)
fig.update_layout(
    autosize=True,
    width=850,
    height=600,
    #xaxis=dict(showgrid=False),
    #yaxis=dict(showgrid=False),
    plot_bgcolor='#e7f6f2',       #setting bgcolor
    paper_bgcolor="#a5c9ca",
)
fig.update_xaxes(rangeselector_activecolor='#F15412')
fig.update_xaxes(color='#1A4D2E')
fig.update_xaxes(gridcolor='#EEEEEE')
fig.update_yaxes(gridcolor='#EEEEEE')
fig.update_xaxes(rangeslider_visible=True,
                rangeselector=dict(
                buttons=list([
                    dict(count=1,label="1m",step='month',stepmode='backward'),
                    dict(count=2,label="2m",step='month',stepmode='backward'),
                    dict(count=3,label="3m",step='month',stepmode='backward'),
                    dict(count=4,label="6m",step='year',stepmode='backward'),
                    dict(count=5,label="1y",step="year",stepmode='backward'),

                    dict(step='all')
                ])))
st.plotly_chart(fig)
st.markdown("---")
st.header("Results :")
day_1 = pd.to_datetime('2022-06-28').date()
output=final.loc[day_1:date,'Forecast']
output = pd.DataFrame(output)
output.index = output.index.strftime('%d %b %Y')
output = output.rename({'Forecast':"Forecasted OIL Prices($)"},axis='columns')
st._legacy_dataframe(output)
st.markdown("---")



st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")





#st.markdown("---")
st.markdown("- Developed by `SKY`.   ⇨[github ](https://github.com/suraj4502), [Linkedin](https://www.linkedin.com/in/surajkumar-yadav-6ab2011a4/), [Ig](https://www.instagram.com/suraj452/).")
#st.markdown("---")