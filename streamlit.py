import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data

dataset = data.dataset

with st.container(border=True, gap=None): #top header
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")


c1 = st.container(border=True)
c1.write(dataset) #display dataset

col1, col2 = st.columns(2) #textinput + query output
budgetinp=col1.text_input(label="Budget",placeholder="Budget")
budgetreginp=col1.selectbox(
  "Region:", 
  data.query("
  SELECT distinct CouncilArea 
  FROM dataset"), 
  placeholder="Select region",
)
#budgetreginp=col1.text_input(label="Region")
if st.button("Budget stuff"):
  regionB = budgetreginp
  pricevarB = str(budgetinp)
  st.write(regionB, pricevarB)
  st.write(data.query("select *, "+pricevarB+"-price as Budget_deviation, price FROM dataset  WHERE CouncilArea = \""+regionB+"\" order by ABS(Budget_deviation) LIMIT 15 "))
  






























































