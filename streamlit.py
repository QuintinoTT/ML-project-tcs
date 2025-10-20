import streamlit as st
import pandas as pd
from thatonefile import datasetcall


st.write("Melbourne housing")
if st.button("test"):
   st.dataframe(datasetcall())

   st.area_chart(tof.dataset ,x="testx", y="testy")




