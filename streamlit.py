import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data


st.header("Melbourne housing", horizontal_alignment="left", vertical_alignment="top")
st.container(data.dataset)


