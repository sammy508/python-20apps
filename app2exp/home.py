import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
description = """
loremipsunkfkjef ieofj kfmkjdsjdhf uiwef er kewjhfcndiuw hoiud-0 doi odi oiudshu ew=ep dfuclk = -fsdj doiu    funckl 0 woiefhr gfh cdvoorwe0[wpoe kjsdfhjdsfb fhfjsdhfus
fkhsdfhs dufh sdf
fhkjsdhf ksjdnf 'f
f kkjdf eufoer hfvfdfhbdsfmwoeiqpwoiewkjeghr  fjhfjfheiooewkdpwos-w mdiurfei feklr jfoi eryfnsdncwlefu93eo fekc ]
"""
st.write(description)

st.subheader("Our Team")

df = pandas.read_csv("01 data.csv", sep=",")
col1, col2, col3 = st.columns(3, gap="medium")


for index, row in df[0:4].iterrows():

    with col1:
        # st.title(row["ffirst name"]+["last name"])
        st.subheader(f"{row["firstname"]} {row['lastname']}")
        st.write(row['role'])
        st.image(f"images/"+ row["image"])


for index, row in df[4:8].iterrows():

    with col2:
        # st.title(row["ffirst name"]+["last name"])
        st.subheader(f"{row["firstname"]} {row['lastname']}")
        st.write(row['role'])
        st.image(f"images/"+ row["image"])


for index, row in df[8:].iterrows():

    with col3:
        # st.title(row["ffirst name"]+["last name"])
        st.subheader(f"{row["firstname"]} {row['lastname']}")
        st.write(row['role'])
        st.image(f"images/"+ row["image"])

