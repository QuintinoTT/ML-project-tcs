import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data

dataset = data.dataset

with st.container(border=True, gap=None): #top header
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")


with st.container(border=True): #fist query; price prediction
  st.subheader("Price prediction:")
  feature_col, data_col = st.columns(2)
  select_type = feature_col.selectbox(
    "Type:", 
    data.query(
      "SELECT distinct Type FROM dataset"), 
    placeholder="Select type",
  )
  select_rooms = feature_col.text_input(label="Amount of rooms:")

  data_col.write(dataset)


with st.container(border=True): #second query
  col1, col2 = st.columns(2, width="stretch")
  col1.write(dataset) #display dataset
  budgetinp=st.text_input(label="Budget:",placeholder="Select budget")
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


st.write(data.query(
  "SELECT distinct Type, Method, Distance, Bedroom2, bathroom, Car, Landsize, YearBuilt, CouncilArea FROM dataset"
))

















