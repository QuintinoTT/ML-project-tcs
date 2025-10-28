import streamlit as st
import pandas as pd
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
