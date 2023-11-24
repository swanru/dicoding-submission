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
# Aotizhongxin  
# Changping  
# Dingling  
# Dongsi 
# Guanyuan 
# Gucheng  
# Nongzhanguan  
# Shunyi 
# Tiantan  
# Wanliu 
# Wanshouxigong 

def Aotizhongxin_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Aotizhongxin.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Aotizhongxin.isna().sum())
    with tab2:
        Aotizhongxin.dropna(axis=0,inplace=True)
        st.text(Aotizhongxin.isna().sum())
def Changping_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Changping.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Changping.isna().sum())
    with tab2:
        Changping.dropna(axis=0,inplace=True)
        st.text(Changping.isna().sum())
def Dingling_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Dingling.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Dingling.isna().sum())
    with tab2:
        Dingling.dropna(axis=0,inplace=True)
        st.text(Dingling.isna().sum())
def Dongsi_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Dongsi.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Dongsi.isna().sum())
    with tab2:
        Dongsi.dropna(axis=0,inplace=True)
        st.text(Dongsi.isna().sum())
def Guanyuan_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Guanyuan.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Guanyuan.isna().sum())
    with tab2:
        Guanyuan.dropna(axis=0,inplace=True)
        st.text(Guanyuan.isna().sum())
def Gucheng_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Gucheng.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Gucheng.isna().sum())
    with tab2:
        Gucheng.dropna(axis=0,inplace=True)
        st.text(Gucheng.isna().sum())
def Nongzhanguan_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Nongzhanguan.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Nongzhanguan.isna().sum())
    with tab2:
        Nongzhanguan.dropna(axis=0,inplace=True)
        st.text(Nongzhanguan.isna().sum())
def Shunyi_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Shunyi.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Shunyi.isna().sum())
    with tab2:
        Shunyi.dropna(axis=0,inplace=True)
        st.text(Shunyi.isna().sum())
def Tiantan_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Tiantan.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Tiantan.isna().sum())
    with tab2:
        Tiantan.dropna(axis=0,inplace=True)
        st.text(Tiantan.isna().sum())
def Wanliu_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Wanliu.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Wanliu.isna().sum())
    with tab2:
        Wanliu.dropna(axis=0,inplace=True)
        st.text(Wanliu.isna().sum())
def Wanshouxigong_(): 
    st.title("Assessing Data")
    buffer = io.StringIO()
    Wanshouxigong.info(buf=buffer)
    values = buffer.getvalue()
    st.text(values)
    st.title("Cleaning Data")
    tab1,tab2 = st.tabs(["Data sebelum dicleaning","Data setelah dicleaning"])
    with tab1:
        st.text(Wanshouxigong.isna().sum())
    with tab2:
        Wanshouxigong.dropna(axis=0,inplace=True)
        st.text(Wanshouxigong.isna().sum())

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
    
    #     st.write("Masuk")
    dataset = pd.concat(data)
    region = st.selectbox("Select Station",station)
    if region == "Aotizhongxin":
        st.write(Aotizhongxin.head())
        Aotizhongxin_()
    elif region == "Changping":
        st.write(Changping.head())
        Changping_()          
    elif region == "Dingling":
        st.write(Dingling.head())
        Dingling_()  
    elif region == "Dongsi":
        st.write(Dongsi.head())
        Dongsi_()
    elif region == "Guanyuan":
        st.write(Guanyuan.head())
        Guanyuan_()
    elif region == "Gucheng":
        st.write(Gucheng.head())
        Gucheng_()
    elif region == "Nongzhanguan":
        st.write(Nongzhanguan.head())
        Nongzhanguan_()
    elif region == "Shunyi":
        st.write(Shunyi.head())
        Shunyi_()
    elif region == "Tiantan":
        st.write(Tiantan.head())
        Tiantan_()
    elif region == "Wanliu":
        st.write(Wanliu.head())
        Wanliu_()
    elif region == "Wanshouxigong":
        st.write(Wanshouxigong.head())  
        Wanshouxigong_()

    
    # tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11= st.tabs(["Aotizhongxin" ,"Changping" ,"Dingling" ,"Dongsi","Guanyuan","Gucheng" ,"Nongzhanguan" ,"Shunyi","Tiantan" ,"Wanliu","Wanshouxigong"])
    # with tab1:
    #     st.write(Aotizhongxin.head())
    # with tab2:
    #     st.write(Changping .head( ))
    # with tab3:
    #     st.write("ASD")
    # with tab4:
    #     st.write("ASD")
    # with tab5:
    #     st.write("ASD")
    # with tab6:
    #     st.write("ASD")
    # with tab7:
    #     st.write("ASD")
    # with tab8:
    #     st.write("ASD")
    # with tab9:
    #     st.write("ASD")
    # with tab10:
    #     st.write("ASD")
    # with tab11:
    #     st.write("ASD")
st.title('Gathering Data')
data()