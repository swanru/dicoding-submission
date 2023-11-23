from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.hello.utils import show_code
import plotly.express as px
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


def data():
    data = [Aotizhongxin,Changping,Dingling,Dongsi,Guanyuan,Gucheng,Nongzhanguan,Shunyi,Tiantan,Wanliu,Wanshouxigong]
    dataset = pd.concat(data)
    st.write("Dataset",dataset.head())
    tab1, tab2 = st.tabs(["Korelasi Data","Kualitas Udara"])
    # tab1
    with tab1:
        Pollution_dataset = dataset[['PM2.5','PM10','SO2','NO2','CO','O3']]
        st.write("Dataset Polutant",Pollution_dataset)
        st.write("Korelasi antar data:")
        korelasi_data = Pollution_dataset.corr()
        st.write(korelasi_data)
        fig,ax=plt.subplots()
        sns.heatmap(korelasi_data,ax=ax)
        st.write(fig)
    # tab2
    with tab2:
        dataset_station = dataset.groupby(by='station').agg({
            'PM2.5':'mean',
            'PM10':'mean',
            'SO2':'mean',
            'NO2':'mean',
            'O3':'mean',
            'CO':'mean',
        })
        st.line_chart(dataset_station)
        data = pd.DataFrame(dataset_station)
        High_PM25 = pd.DataFrame(data["PM2.5"].sort_values(ascending=False).reset_index())
        High_PM10 = pd.DataFrame(data["PM10"].sort_values(ascending=False).reset_index()) 
        High_SO2  = pd.DataFrame(data["SO2"].sort_values(ascending=False).reset_index())
        High_NO2  = pd.DataFrame(data["NO2"].sort_values(ascending=False).reset_index())
        High_O3   = pd.DataFrame(data["O3"].sort_values(ascending=False).reset_index())
        High_CO = pd.DataFrame(dataset_station["CO"].sort_values(ascending=False).reset_index())
        st.write(data)
        Hasil = pd.DataFrame({"Data Tertinggi": ["PM 2.5", "PM 10",
                                        "SO2","NO2",
                                        "O3","CO"], 
                      "Kota"          :[High_PM25.station[0], High_PM10.station[0],
                                        High_SO2.station[0], High_NO2.station[0],
                                        High_O3.station[0], High_CO.station[0]],
                      "Nilai"         :[High_PM25["PM2.5"][0], High_PM10.PM10[0],
                                        High_SO2.SO2[0], High_NO2.NO2[0],
                                        High_O3.O3[0], High_CO.CO[0]]})
        Hasil.to_numpy()
        st.write("Data Polutant tertinggi",Hasil)

    

st.title('Dataset Seluruh Kota')
data()