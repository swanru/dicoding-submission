from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
kota = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")


def data():
    st.write("Dataset")
    st.write(kota)



st.title('Kualitas Udara Kota Changping')
data()