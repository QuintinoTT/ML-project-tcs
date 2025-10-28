import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data
import modelthings as model
import influentialmetric as boetmodule
dataset = data.dataset




with st.container(border=True, gap=None): #top header
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")

#querry stuff
with st.container(border=True, gap="Small"):
  sqlquery = st.text_input(label="SQL entry")
  if st.button("Push query"):
    try:
        st.write(data.query(sqlquery))
    except Exception:
      st.write("Invalid Query")
#end

with st.container(border=True): #fist query; price prediction
 with st.container():
  st.subheader("Sale price prediction:")
  one_col, two_col, three_col = st.columns([3,3,3])

  #drop down boxes for price prediction
  select_type = one_col.selectbox(
    "Type:", 
    data.query(
      "SELECT distinct Type FROM dataset"), 
    placeholder="Select type",
  )
  select_councilarea = two_col.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Council area",
  )
  select_method = three_col.selectbox(
    "Method:", 
    data.query(
      "SELECT distinct Method FROM dataset"), 
    placeholder="Select method",
  )

  #text inputs for price prediction
  select_rooms = one_col.text_input(label="Amount of rooms: (1-10)")
  select_distance = two_col.text_input(label="Distance to centre (km): (0-47)")
  select_bedroom = three_col.text_input(label="Amount of bedrooms: (1-10)")
  select_bathroom = one_col.text_input(label="Amount of bathrooms: (1-8)")
  select_car = two_col.text_input(label="Amount of carparking spaces: (0-10)")
  select_landsize = three_col.text_input(label="Landsize (km^2): (<37000)")
  select_yearbuilt = one_col.text_input(label="Year built: (1830-2017)")
  select_propertycount = two_col.text_input(label="Property count: (300-22000)")
 
with st.container(border=False):
 
  if st.button("Estimate"):
 
    Pricebox = st.write(model.model.predict(model.Dealwithinputdata(pd.DataFrame(data={"Rooms": [int(select_rooms)], "Distance": [float(select_distance)], "Bedroom2": [int(select_bedroom)],"Bathroom": [int(select_bathroom)],"Car": [int(select_car)],"Landsize":[float(select_landsize)], "YearBuilt":[int(select_yearbuilt)], "PropertyCount": [int(select_propertycount)], "Type": [select_type], "Method": [select_method],   "CouncilArea": [select_councilarea]}))))
with st.container(border=True): #second query
  st.header("Feature importance estimation")
  inputcolumn, outputcolumn = st.columns([1,3])
  areabox = inputcolumn.selectbox("Choose the area",data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Council area")
  if st.button("List"): 
    him = boetmodule.highest_influence_metric(areabox)(3)
    st.write(pd.DataFrame({"Most Important Features": [him[0][0],him[1][0],him[2][0]]}))




with st.container(border=True): #third query
  st.header("Budget Prediction")

  budgetinp=st.text_input(label="Budget:", placeholder="Select budget")
  budgetreginp=st.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Select region",
  )

  
  if st.button("Check possibilities"):
    regionB = budgetreginp
    pricevarB = str(budgetinp)
    st.write(data.query(
      "SELECT *, "+pricevarB+"-price AS Budget_deviation FROM dataset  WHERE CouncilArea = \""+regionB+"\" ORDER BY ABS(Budget_deviation) LIMIT 15 ")) #change query to select less stuff and sort by price deviation








































































































