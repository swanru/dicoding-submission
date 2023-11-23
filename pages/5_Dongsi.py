from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
kota = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")


def data():
    st.write("Dataset")
    kota.dropna(axis=0,inplace=True)
    st.write(kota.reset_index(drop=True))



st.title('Kualitas Udara Kota Dongsi')
data()