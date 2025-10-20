import streamlit as st
import pandas as pd
import thatonefile as *


st.write("Melbourne housing")
if st.button("test"):
    st.dataframe(datasetcall())

st.area_chart(ds.dataset ,x="testx", y="testy")
