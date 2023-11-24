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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Submission",  
    )

    st.title("Selamat Datang di Dashboard Proyek Analisis Data saya!")
    st.markdown(
        """
        ## Proyek Analisis Data: Dataset Air Quality
        Selamat datang di Proyek Analisis Dicoding
        - Nama        : Shelwan Riaudy U
        - Email       : selwanriaudyu48@gmail.com
        - Id Dicoding : [selwanru](https://www.dicoding.com/users/selwanru/academies)
        ### Menentukan Pertanyaan Bisnis
        1. Bagaimana Kualitas Udara pada setiap kota dalam kurun waktu tertentu ?
        2. Nilai Polutan paling tinggi berdasarkan rata-rata seluruh waktu terdapat pada kota?
        3. Kapan kualitas udara memiliki kualitas terburusk dalam kurun waktu tertentu pada setiap kota berdasarkan Indeks Standar Pencemar Udara?
        ### Library yang dibutuhkan
        - Numpy 
        - Pandas
        - Matplotlib.pyplot
        - Seaborn
        """
    )
if __name__ == "__main__":
    run()
