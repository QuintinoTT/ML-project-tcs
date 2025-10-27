import pandas as pd
from joblib import load
ghostrow = pd.read_csv('ghostframe.csv')
model = load("mdl.joblib")
scaler = load("scale.joblib")
def Dealwithinputdata(dataframe):
  dummiedframe=pd.get_dummies(dataframe)
  ghostrowc = ghostrow.copy()
  print(ghostrowc)
  for columns in ghostrowc:
        if columns in dummiedframe.columns:
           ghostrowc.at[0, columns] = dummiedframe.at[0, columns]
  scaledframe=scaler.transform(ghostrowc)
  return scaledframe 
