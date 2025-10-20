import streamlit as st
import pandas as pd
import thatonefile.py as tof


st.write("Melbourne housing")
if st.button("test"):
    st.dataframe(tof.datasetcall())

st.area_chart(dataset ,x="testx", y="testy")

