import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")
uploaded_image = st.file_uploader("Upload Image")

while uploaded_image:
    file_image = Image.open(uploaded_image)
    conv_img = file_image.convert("L")
    st.image(conv_img)
    break

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)
    st.stop
  