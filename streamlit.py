import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data


st.header("Melbourne housing")
st.container(data.dataset, border="True", key=None, width="stretch", height="content", horizontal=False, horizontal_alignment="left", vertical_alignment="top", gap="small")






