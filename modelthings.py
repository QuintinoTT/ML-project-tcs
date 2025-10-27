import streamlit as st
import pandas as pd
from joblib import load
ghostrow = pd.read_csv('ghostframe.csv')
ghostrow.ghostrow.drop(columns=["Unnamed:0"])
model = load("mdl.joblib")
scaler = load("scale.joblib")
def Dealwithinputdata(dataframe):
  dummiedframe=pd.get_dummies(dataframe)
  dummiedframe.astype(int)
  ghostrowc = ghostrow.copy()
  for columns in ghostrowc:
      if columns in dummiedframe.columns:
         ghostrowc.at[0, columns] = dummiedframe.at[0, columns]
  scaledframe=scaler.transform(ghostrowc)
  return scaledframe 
