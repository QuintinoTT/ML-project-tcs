import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data

with st.container(border=True, height=200):
  st.header("Melbourne housing")
c1 = st.container(border=True)
c1.write(data.dataset)
col1, col2 = st.columns(2)
col1.chat_input(placeholder="testinput")
col1.chat_input(placeholder="testinput2")
col1.chat_input(placeholder="testinput3.1")
col2.chat_input(placeholder="testinput3")
























