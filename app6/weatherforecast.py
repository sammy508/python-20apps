import streamlit as st

st.title("Weather Forecast for Next Days")

place = st.text_input("Place")
days = st.slider("Forecasted Days",min_value=1, max_value=5,   help= "select")

options = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{options} for Next {days} Days in {place}")