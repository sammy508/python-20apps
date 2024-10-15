import streamlit as st

st.header("Contact Me", divider="gray",)

with st.form(key="form"):
    user_email = st.text_input("Your email address ")
    message = st.text_area("Enter your message here ")
    button = st.form_submit_button("Submit")

    if button:
        print(" Oh my gosh")