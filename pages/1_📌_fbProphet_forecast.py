import pandas as pd
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import time
from helper import prophet_data_processor

df = prophet_data_processor('data/RBRTEd.xls')

st.title("Forecasting Using fbProphet.")
st.markdown("---")



with st.spinner(text="Model Training..."):
     time.sleep(10)



model = Prophet()
model.fit(df)


future = model.make_future_dataframe(periods=365)

st.header("👉🏽Results :")
forecast = model.predict(future)
forecast=forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
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

