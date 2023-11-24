from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.hello.utils import show_code
import plotly.express as px
import io
Aotizhongxin = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
Changping = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
Dingling = pd.read_csv("PRSA_Data_Dingling_20130301-20170228.csv")
Dongsi = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")
Guanyuan = pd.read_csv("PRSA_Data_Guanyuan_20130301-20170228.csv")
Gucheng = pd.read_csv("PRSA_Data_Gucheng_20130301-20170228.csv")
Nongzhanguan = pd.read_csv("PRSA_Data_Nongzhanguan_20130301-20170228.csv")
Shunyi = pd.read_csv("PRSA_Data_Shunyi_20130301-20170228.csv")
Tiantan = pd.read_csv("PRSA_Data_Tiantan_20130301-20170228.csv")
Wanliu = pd.read_csv("PRSA_Data_Wanliu_20130301-20170228.csv")
Wanshouxigong = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")	
def Aotizhongxin_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Aotizhongxin.dropna(axis=0,inplace=True)
    st.write(Aotizhongxin.describe(include="all"))
    Pollution_dataset = Aotizhongxin[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Changping_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Changping.dropna(axis=0,inplace=True)
    st.write(Changping.describe(include="all"))
    Pollution_dataset = Changping[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Dingling_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Dingling.dropna(axis=0,inplace=True)
    st.write(Dingling.describe(include="all"))
    Pollution_dataset = Dingling[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Dongsi_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Dongsi.dropna(axis=0,inplace=True)
    st.write(Dongsi.describe(include="all"))
    Pollution_dataset = Dongsi[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Guanyuan_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Guanyuan.dropna(axis=0,inplace=True)
    st.write(Guanyuan.describe(include="all"))
    Pollution_dataset = Guanyuan[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Gucheng_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Gucheng.dropna(axis=0,inplace=True)
    st.write(Gucheng.describe(include="all"))
    Pollution_dataset = Gucheng[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Nongzhanguan_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Nongzhanguan.dropna(axis=0,inplace=True)
    st.write(Nongzhanguan.describe(include="all"))
    Pollution_dataset = Nongzhanguan[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Shunyi_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Shunyi.dropna(axis=0,inplace=True)
    st.write(Shunyi.describe(include="all"))
    Pollution_dataset = Shunyi[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Tiantan_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Tiantan.dropna(axis=0,inplace=True)
    st.write(Tiantan.describe(include="all"))
    Pollution_dataset = Tiantan[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Wanliu_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Wanliu.dropna(axis=0,inplace=True)
    st.write(Wanliu.describe(include="all"))
    Pollution_dataset = Wanliu[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def Wanshouxigong_(): 
    st.title("Explorasi data pada dataset untuk setiap column")
    Wanshouxigong.dropna(axis=0,inplace=True)
    st.write(Wanshouxigong.describe(include="all"))
    Pollution_dataset = Wanshouxigong[['PM2.5','PM10','SO2','NO2','CO','O3']]
    korelasi_data = Pollution_dataset.corr()
    fig,ax=plt.subplots()
    sns.heatmap(korelasi_data,ax=ax)
    st.title("Korelasi Data")
    tab1, tab2 = st.tabs(["Nilai Korelasi","Heat Map"])
    with tab1:
        st.write(korelasi_data)
    with tab2:
        fig
def data():
    data = [Aotizhongxin,Changping,Dingling,Dongsi,Guanyuan,Gucheng,Nongzhanguan,Shunyi,Tiantan,Wanliu,Wanshouxigong]
    station = {
        "Aotizhongxin",
        "Changping",
        "Dingling",
        "Dongsi",
        "Guanyuan",
        "Gucheng ",
        "Nongzhanguan",
        "Shunyi",
        "Tiantan",
        "Wanliu",
        "Wanshouxigong"
    }
    dataset = pd.concat(data)
    st.title("Exploratory Data Analysis")
    region = st.selectbox("Select Station",station)
    if region == "Aotizhongxin":
        Aotizhongxin_()
    elif region == "Changping":
        Changping_()          
    elif region == "Dingling":
        Dingling_()  
    elif region == "Dongsi":
        Dongsi_()
    elif region == "Guanyuan":
        Guanyuan_()
    elif region == "Gucheng":
        Gucheng_()
    elif region == "Nongzhanguan":
        Nongzhanguan_()
    elif region == "Shunyi":
        Shunyi_()
    elif region == "Tiantan":
        Tiantan_()
    elif region == "Wanliu":
        Wanliu_()
    elif region == "Wanshouxigong": 
        Wanshouxigong_()
data()