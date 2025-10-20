import streamlit as st
import pandas as pd
import thatonefile as tof


st.write("Melbourne housing")
if st.button("test"):
    st.dataframe(tof.datasetcall())

st.area_chart(ds.dataset ,x="testx", y="testy")

