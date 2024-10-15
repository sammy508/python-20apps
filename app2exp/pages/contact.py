import streamlit as st

st.title("Contact Us",anchor=None)
with st.form(key="form"):
    st.text_input("Enter  gmail")
    st.text_area("Enter your text")
    st.form_submit_button("Submit")