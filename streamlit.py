import streamlit as st
import pandas as pd
import thatonefile as ds


st.write("Melbourne housing")
if st.button("test"):
    st.write("test complete")
st.area_chart(ds.dataset ,x="testx", y="testy")