import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data

dataset = data.dataset

with st.container(border=True, gap=None): #top header
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")

with st.container(border=True):
  col1, col2 = st.columns(2, width="Stretch")
  col1.write(dataset) #display dataset
  budgetinp=st.text_input(label="Budget",placeholder="Budget")
  budgetreginp=st.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Select region",
  )
  if st.button("Budget stuff"):
    regionB = budgetreginp
    pricevarB = str(budgetinp)
    col2.write(data.query(
      "SELECT *, "+pricevarB+"-price AS Budget_deviation FROM dataset  WHERE CouncilArea = \""+regionB+"\" ORDER BY ABS(Budget_deviation) LIMIT 15 ")) #change query to select less stuff and sort by price deviation

















