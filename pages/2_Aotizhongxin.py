from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
kota = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")


def data():
    st.write("Dataset")
    st.write(kota.head())
    tab1, tab2 ,tab3 = st.tabs(["Dataset", "Korelasi Data","Kualitas Udara"])
    with tab1:
        st.title("slebw")
    with tab2:
        st.title("slebw")
    with tab3:
        st.write(
            """
            ## Data Pollutan
            Data polutan yang digunakan pada penelitian ini adalah PM10, PM2.5, O3, NO2, SO2, CO
            """
        )
        Pollution = kota[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution['date'] = pd.to_datetime(Pollution[['year','month','day']])
        st.write(Pollution.head())

        tab_1,tab_2,tab_3,tab_4 = st.tabs(["Tahunan", "Bulanan","30 Hari","Setiap Jam"])
        
        with tab_1:
            st.title("slebw")
        with tab_2:
            st.title("slebw")
        with tab_3:
            st.title("slebw")
        with tab_4:
            st.title("slebw")    
        # dataset_year = kota.groupby(by='year').agg({
        #     'PM10':'mean',
        #     'PM2.5':'mean',
        #     'O3':'mean',
        #     'NO2':'mean',
        #     'SO2':'mean',
        # })
        # dataset_month = kota.groupby(by='month').agg({
        #     'PM10':'mean',
        #     'PM2.5':'mean',
        #     'O3':'mean',
        #     'NO2':'mean',
        #     'SO2':'mean',
        # })
        # dataset_day = kota.groupby(by='day').agg({
        #     'PM10':'mean',
        #     'PM2.5':'mean',
        #     'O3':'mean',
        #     'NO2':'mean',
        #     'SO2':'mean',
        # })
        # dataset_hour = kota.groupby(by='hour').agg({
        #     'PM10':'mean',
        #     'PM2.5':'mean',
        #     'O3':'mean',
        #     'NO2':'mean',
        #     'SO2':'mean',
        # })


st.title('Kualitas Udara Kota Aotizhongxin')
data()