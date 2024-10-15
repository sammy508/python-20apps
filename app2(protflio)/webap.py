import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image('images/photo.png')  


with col2:
    st.title("Sammy Cpgn")    

    content = """My name is samir cpgn. I live in butwal and i am a bca student. I study bca on crimson colllege and i oftemly visit colleges. Mine collegus call me Einstein
    and and I love to travel a lots """
    st.info(content)

content2 = """ Below you can find si=ome other project like stuffs and more other beginner projects """
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv("006 data.csv", sep=";")
# with col3 :
#     for index, row in df[0:10] .iterrows():
#         st.header(row["title"])

# with col4 :
#     for index, row in df[10:] .iterrows():
#         st.header(row["title"])




col5, col6 = st.columns(2,gap="large")


for index, row in df[0:10].iterrows():
    with col5:
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/"+ row["image"])    # Here images are on image folder but
        # its name are included on csv file so we abstract name from csv file and gave a images/ to provide image folder path #

        st.write(f"[Source code]({row["url"]})")

for index, row in df[10:].iterrows():
    with col6:
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/"+ row["image"])   
        st.write(f"[Source code]({row["url"]})")
       