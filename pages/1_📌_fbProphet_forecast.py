import pandas as pd
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.express as px
import plotly.graph_objects as go
import pickle
from helper import prophet_data_processor

st.title("Forecasting Using fbProphet.")
st.markdown("---")


with open(r'Models\prophet_model.pkl', 'rb') as f:
    model= pickle.load(f)

future = model.make_future_dataframe(periods=365)

st.header("👉🏽Results :")
forecast = model.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
st.dataframe(forecast[forecast['ds']>'2023-06-26 00:00:00'])


st.header("👉🏽Result Chart :")

# Plot the forecast
fig_forecast = plot_plotly(model, forecast)
fig_forecast.update_layout(
    width=700,  # Adjust the width as desired
    height=500,  # Adjust the height as desired,
)
fig_forecast.update_xaxes(range=[forecast['ds'][9130], forecast['ds'][9525]])
st.plotly_chart(fig_forecast)


st.markdown('---')
st.header("👉🏽Components :")
# Plot the components
fig_components = plot_components_plotly(model, forecast)
fig_components.update_layout(
    width=700,  # Adjust the width as desired
    height=500,  # Adjust the height as desired,
)
st.plotly_chart(fig_components)

