import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Visualization')
data = pd.read_csv('cleanedData.csv')
tab1, tab2, tab3 = st.tabs(["Tourism over Time vs Region", "Tourism over Time vs Prupose", "Tourism over Time vs Mode of Travel"])
with tab1:
    column = ['FromAfrica', 'FromEastAsiaandthePacific', 'FromEurope', 'FromSouthAsia']
    st.line_chart(
        data,
        x="year",
        y=column
    )

with tab2:
    column = ['Personal(Visit)', 'BusinessAndProfessional(Visit)']
    st.line_chart(
        data,
        x="year",
        y=column
    )

with tab3:
    column = ['Air(Travel)', 'Land(Travel)']
    st.line_chart(
        data,
        x="year",
        y=column
    )