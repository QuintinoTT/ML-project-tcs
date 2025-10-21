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
  feature_col, data_col = st.columns(2 ,[1,3])
  select_type = feature_col.selectbox(
    "Type:", 
    data.query(
      "SELECT distinct Type FROM dataset"), 
    placeholder="Select type",
  )
  select_rooms = feature_col.text_input(label="Amount of rooms:")
  select_method = feature_col.selectbox(
    "Method:", 
    data.query(
      "SELECT distinct Method FROM dataset"), 
    placeholder="Select method",
  )
  select_distance = feature_col.text_input(label="Distance to centre:")
  select_bedroom = feature_col.text_input(label="Amount of bedrooms:")
  select_bathroom = feature_col.text_input(label="Amount of bathrooms:")
  select_car = feature_col.text_input(label="Amount of carparking spaces:")
  select_landsize = feature_col.text_input(label="Landsize:")
  select_yearbuilt = feature_col.text_input(label="Year built:")
  select_councilarea = feature_col.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Council area",
  )
  select_propertycount = feature_col.text_input(label="Amount of property in area")
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

















