import streamlit as st
from PIL import Image

with st.expander("start camera"):
    camera_img = st.camera_input("camera")  # access camera 

while camera_img:  # it execute only the above condition is true 

    img = Image.open(camera_img, "r") # create a pillow image instance

    gray_img = img.convert("L")   # convert image to gray_scale

    st.image(gray_img)   # Render gray image to web

    # 9846160606