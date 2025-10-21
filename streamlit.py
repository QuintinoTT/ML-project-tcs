import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data


st.container()
st.header("Melbourne housing")
st.write(data.dataset)


