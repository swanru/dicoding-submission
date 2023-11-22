# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
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
def data_frame():
    st.write(Aotizhongxin.head())
#     try:


# # def data_frame_demo():
# #     @st.cache_data
# #     def get_UN_data():
# #         AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
# #         df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
# #         return df.set_index("Region")

# #     try:
# #         df = get_UN_data()
# #         countries = st.multiselect(
# #             "Choose countries", list(df.index), ["China", "United States of America"]
# #         )
# #         if not countries:
# #             st.error("Please select at least one country.")
# #         else:
# #             data = df.loc[countries]
# #             data /= 1000000.0
# #             st.write("### Gross Agricultural Production ($B)", data.sort_index())

# #             data = data.T.reset_index()
# #             data = pd.melt(data, id_vars=["index"]).rename(
# #                 columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
# #             )
# #             chart = (
# #                 alt.Chart(data)
# #                 .mark_area(opacity=0.3)
# #                 .encode(
# #                     x="year:T",
# #                     y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
# #                     color="Region:N",
# #                 )
# #             )
# #             st.altair_chart(chart, use_container_width=True)
# #     except URLError as e:
# #         st.error(
# #             """
# #             **This demo requires internet access.**
# #             Connection error: %s
# #         """
# #             % e.reason
# #         )


# st.set_page_config(page_title="DataFrame Demo", page_icon="📊")
# st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

data_frame()

show_code(data_frame)
