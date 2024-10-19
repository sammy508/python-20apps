import requests
import streamlit as st

url ="https://api.nasa.gov/planetary/apod?api_key=DE4C1kb8uAl2Pok1ZsBMYnWf9DbnC5K0Vv5F7Oba"
# "https://api.nasa.gov/planetary/apod&apiKey=DE4C1kb8uAl2Pok1ZsBMYnWf9DbnC5K0Vv5F7Oba"

request = requests.get(url)

content = request.json()


title = content['title']
image = content['url']
description = content['explanation']

st.title(title)
st.image(image)
st.write(description)