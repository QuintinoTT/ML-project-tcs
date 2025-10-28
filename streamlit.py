import streamlit as st
import pandas as pd
import sklearn as sl
import pandasql as ps
import dataprocessing as data
from joblib import load
ghostrow = pd.read_csv('ghostframe.csv')

model = load("model.joblib")
scaler = load("scalr.joblib")
def Dealwithinputdata(dataframe):
  dummiedframe=pd.get_dummies(dataframe)

  ghostrowc = ghostrow.copy()

  for columns in ghostrowc:
      if columns in dummiedframe.columns:
         ghostrowc.at[0, columns] = dummiedframe.at[0, columns]
  ghostrowc=ghostrowc.drop(columns=["Unnamed: 0"])
  scaledframe=scaler.transform(ghostrowc)
  return scaledframe

dataset = data.dataset
#querry stuff
with st.container(border=True, gap="Small"):
  sqlquery = st.text_input(label="temperary SQL on web app (invalid query will break the website)", placeholder="write your SQL query here")
  if st.button("push query"):
    try:
        st.write(data.query(sqlquery))
    except Exception:
      st.write("nah")
#end



with st.container(border=True, gap=None): #top header
  st.header("Melbourne housing", divider="blue")
  st.write("Predicting housing prices using kNN Machine Learning")


with st.container(border=True): #fist query; price prediction
  st.subheader("Sale price prediction:")
  feature_col, data_col = st.columns([1,3])

  #drop down boxes for price prediction
  select_type = feature_col.selectbox(
    "Type:", 
    data.query(
      "SELECT distinct Type FROM dataset"), 
    placeholder="Select type",
  )
  select_councilarea = feature_col.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Council area",
  )
  select_method = feature_col.selectbox(
    "Method:", 
    data.query(
      "SELECT distinct Method FROM dataset"), 
    placeholder="Select method",
  )

  #text inputs for price prediction
  select_rooms = feature_col.text_input(label="Amount of rooms:")
  select_distance = feature_col.text_input(label="Distance to centre:")
  select_bedroom = feature_col.text_input(label="Amount of bedrooms:")
  select_bathroom = feature_col.text_input(label="Amount of bathrooms:")
  select_car = feature_col.text_input(label="Amount of carparking spaces:")
  select_landsize = feature_col.text_input(label="Landsize:")
  select_yearbuilt = feature_col.text_input(label="Year built:")
  select_propertycount = feature_col.text_input(label="Property count:")
  data_col.write(dataset)
  if st.button("Estimate"):
  # st.write(select_rooms, select_distance, select_landsize)
   #newframe=Dealwithinputdata(pd.DataFrame(data={"Rooms": [2], "Distance": [20], "Bedroom2": [2],"Bathroom": [2],"Car": [0],"Landsize":[2], "YearBuilt":[2], "PropertyCount": [2], "Type": ['h'], "Method": ["S"],  "CouncilArea": ["Yarra"]}))
  # st.write(model.predict(Dealwithinputdata

    Pricebox = st.write(model.predict(Dealwithinputdata(pd.DataFrame(data={"Rooms": [select_rooms], "Distance": [select_distance], "Bedroom2": [select_bedroom],"Bathroom": [select_bathroom],"Car": [select_car],"Landsize":[select_landsize], "YearBuilt":[select_yearbuilt], "PropertyCount": [select_propertycount], "Type": [select_type], "Method": [select_method],   "CouncilArea": [select_councilarea]}))))
  
with st.container(border=True): #second query
  st.header("Feature importance estimation")
  inputcolumn, outputcolumn = st.columns([1,3])
  areabox = inputcolumn.selectbox("e", data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Council area")
  




with st.container(border=True): #third query
 # st.header("Budget Prediction")
  st.write(dataset) #display dataset
  budgetinp=st.text_input(label="Budget:", placeholder="Select budget")
  budgetreginp=st.selectbox(
    "Region:", 
    data.query(
      "SELECT distinct CouncilArea FROM dataset"), 
    placeholder="Select region",
  )

  
  if st.button("Budget stuff"):
    regionB = budgetreginp
    pricevarB = str(budgetinp)
    st.write(data.query(
      "SELECT *, "+pricevarB+"-price AS Budget_deviation FROM dataset  WHERE CouncilArea = \""+regionB+"\" ORDER BY ABS(Budget_deviation) LIMIT 15 ")) #change query to select less stuff and sort by price deviation








































































