from joblib import load
model = load("knn_model_price_prediction.joblib")
scaler = load("scaler_price_prediction.joblib")
def dataframescale(dataframe):
  scaledframe=scaler.transform(dataframe)
  return scaledframe
