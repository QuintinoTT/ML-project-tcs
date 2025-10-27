import pandas as pd
from joblib import load
model = load("knn_model_price_prediction.joblib")
scaler = load("scaler_price_prediction.joblib")
def Dealwithinputdata(dataframe):
  dummiedframe=pd.get_dummies(dataframe)
  
  scaledframe=scaler.transform(dataframe)
  return scaledframe 
