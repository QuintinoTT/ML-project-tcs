import pandas as pd
import pandasql as ps
import sklearn.model_selection as skl
from sklearn.preprocessing import StandardScaler

dataset_path = 'dataset.csv'
dataset = pd.read_csv(dataset_path)

dataset = dataset.drop(columns=['Address', 'BuildingArea', 'Suburb', 'Postcode','Date', 'Lattitude', 'Longtitude', 'Regionname'])

def query(sql):
    return ps.sqldf(sql, globals())




for i, row in dataset.iterrows():
    if row['Landsize'] == 0:
        dataset = dataset.drop([i])

dataset = dataset.dropna()





print(query("""
SELECT Landsize FROM dataset
WHERE Landsize >= 0
Order by Landsize DESC
"""))
dataset_encoded = pd.get_dummies(dataset)
dataset_encoded.astype(int)

price = dataset_encoded.Price
dataset_features = dataset_encoded.drop(columns=['Price'])

dataset_features_train, dataset_features_train, price_train, price_test = skl.train_test_split(dataset_features, price, test_size=0.2, random_state=42)


scaler = StandardScaler()
dataset_features_train_scaled = pd.DataFrame(scaler.fit_transform(dataset_features_train), columns=dataset_features_train.columns)
dataset_features_test_scaled = pd.DataFrame(scaler.transform(dataset_features_train), columns=dataset_features_train.columns)

print(dataset)
dataset.to_csv('C:/Users/lucas/Documents/Project week 7 & 8/cleaned_md.csv', index=False)
print("Cleaned dataset saved to 'cleaned_md.csv'")
def datasetcall():
    return dataset
