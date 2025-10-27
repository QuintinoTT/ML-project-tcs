import streamlit as st
import pandas as pd
from joblib import load
ghostrow = pd.read_csv('ghostframe.csv')
print(
model = load("mdl.joblib")
scaler = load("scale.joblib")
def Dealwithinputdata(dataframe):
  dummiedframe=pd.get_dummies(dataframe)
  dummiedframe.astype(int)
  ghostrowc = ghostrow.copy()
 
  return ghostrowc 
