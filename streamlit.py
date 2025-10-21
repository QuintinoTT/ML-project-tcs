import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data

with st.container(border=True, gap=None):
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")
c1 = st.container(border=True)
c1.write(data.dataset)
col1, col2 = st.columns(2)
budgetinp=col1.chat_input(placeholder="testinput")
budgetreginp=col1.chat_input(placeholder="testinput2")
col1.chat_input(placeholder="testinput3.1")
col2.chat_input(placeholder="testinput3")
if st.button("Budget stuff"):
  regionB = budgetreginp
  pricevarB = budgetinp
  st.write(data.query("select *, "+pricevarB+"-price as Budget_deviation, price FROM dataset  WHERE CouncilArea = \""+regionB+"\" order by ABS(Budget_deviation) LIMIT 15 "))
  




































