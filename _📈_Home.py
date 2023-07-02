import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import datetime
import helper
image = Image.open('data/Images/img_1_4.jpg')

st.set_page_config(page_title='Oil price Forecasting', page_icon='📈', layout="centered", initial_sidebar_state="expanded", menu_items=None)
#
st.cache()
df = helper.data_preprocessor('data/RBRTEd.xls')

st.title("Forecasting Crude oil prices 📈 ")
st.markdown('---')
st.image(image)
st.markdown('---')


#data preprocessing
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


combined_df = pd.concat([df_past, df_future])
combined_df.set_index('Date', inplace=True)
end_date = st.sidebar.date_input("#### Enter the date till you want your Forecast: ")
end_datetime = datetime.datetime.combine(end_date, datetime.datetime.min.time())

final = combined_df[combined_df.index <= end_datetime]  # final stores all the values from starting till you want [input you give]



# plotting forecasted.
st.header("Forecasted Prices 💲 : ")
fig = px.line(data_frame=final, y=['Actual', 'Forecast'],
              color_discrete_sequence=['#5D9C59', '#FF8400'])
fig.update_layout(
    autosize=True,
    width=850,
    height=600,
    plot_bgcolor='white',
    paper_bgcolor="#a5c9ca")
fig.update_xaxes(rangeselector_activecolor='#F15412')
fig.update_xaxes(color='#1A4D2E')
fig.update_xaxes(gridcolor='#EEEEEE')
fig.update_yaxes(title='price',gridcolor='#EEEEEE')
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step='month', stepmode='backward', visible=True),
            dict(count=2, label="2m", step='month', stepmode='backward', visible=True),
            dict(count=3, label="3m", step='month', stepmode='backward', visible=True),
            dict(count=4, label="6m", step='year', stepmode='backward', visible=True),
            dict(count=5, label="1y", step="year", stepmode='backward', visible=True),
            dict(step='all', visible=True)
        ])
    )
)
st.plotly_chart(fig)
st.markdown("---")


#plotting table
st.header("Results 🛢️ :")


date_1 = pd.to_datetime('2023-06-26').date()
output = final.loc[date_1:final.index[-1], 'Forecast']
output = pd.DataFrame(output)
output.index = output.index.strftime('%d %b %Y')
output = output.rename(columns={'Forecast': 'Forecasted OIL Prices($)'})
st.dataframe(output)



# fig = go.Figure(data=[go.Table(
#     header=dict(values=list(['Date','Forecasted OIL Prices($)']),
#                 fill_color='#F7E6C4',
#                 align='center'),
#     cells=dict(values=[output.index,output['Forecasted OIL Prices($)']],
#                fill_color='#FFF4F4',
#                align='center'))
# ])
# st.plotly_chart(fig)
st.markdown("---")




st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")







#st.markdown("---")
st.sidebar.markdown("- Developed by `SKY`.   ⇨[github ](https://github.com/suraj4502), [Linkedin](https://www.linkedin.com/in/suraj4502), [Ig](https://www.instagram.com/suraj452/).")
#st.markdown("---")