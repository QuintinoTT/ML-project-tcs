from collections import Counter
import pandas as pd
import sklearn.model_selection as skl
from sklearn.preprocessing import StandardScaler
from joblib import load

# Load the saved model and scaler
knn_reg_loaded = load(
    "model.joblib")
scaler_loaded = load(
    "scalr.joblib")

# Modify the path according to where the file is in your filesystem
dataset = pd.read_csv(
    "dataset.csv")

# Clean up the dataset
dataset = dataset.drop(columns=['Address', 'BuildingArea', 'Suburb',
                       'Postcode', 'Date', 'Lattitude', 'Longtitude', 'Regionname', 'Price','SellerG'])

for i, row in dataset.iterrows():
    if row['Landsize'] == 0:
        dataset = dataset.drop([i])

dataset = dataset.dropna()

# Select numeric columns (int or float)
numeric_columns = dataset.select_dtypes(
    include=['int64', 'float64']).columns.tolist()

# Select non-numeric columns
non_numeric_columns = dataset.select_dtypes(
    exclude=['int64', 'float64']).columns.tolist()

# Convert categorical columns to numerical using one-hot encoding
dataset_encoded = pd.get_dummies(
    dataset, columns=non_numeric_columns, drop_first=True)

dataset_encsca = scaler_loaded.transform(dataset_encoded)

# Gets used in the function highest_influence_metric()


# Expects the name of a region as string
def highest_influence_metric(council_area):

    i = 0
    for col in dataset_encoded.columns:
        if col == f"CouncilArea_{council_area}":
            area_index = i
        i = i+1

    area_index_decr = area_index + 1
    print(area_index)
    print(dataset_encsca[69][area_index_decr])

    list_metrics = []

    council_area_encoded = f"CouncilArea_{council_area}"
    # print(council_area_encoded)
    # print(dataset_encoded.head())
    # if council_area_encoded is not dataset_encoded.columns:
    #     return "{council_area} is not in dataset"

    # Dataset still needs to be provided


    if council_area_encoded not in dataset_encoded.columns:
        return "{council_area} is not present in dataset"

    i = 0
    while i < len(dataset_encsca):

        list_predictions = []

        # Algorithm to make a list of all predicted values if you corrupt each column of a row 1 by one
        if dataset_encsca[i][area_index] > 0:

            # Corrupt the metric, make a prediction, store that prediction in a list and then restore the corrupted value
            # It does this for each value in the row
            ind = 0
            while ind < len(dataset_encsca[i]):
                if "CouncilArea" not in dataset_encoded.columns[ind]:
                    corrupt_row = dataset_encsca[i]
                    corrupt_row[ind] = corrupt_row[ind] * 1000

                    prediction = knn_reg_loaded.predict(corrupt_row.reshape(1, -1))
                    list_predictions.append(prediction)

                ind = ind+1

            # Find the index value of the metric which influenced the price the most
            res = max(list_predictions)
            index = list_predictions.index(res)

            # Make a list of all the metrics that were most important in a specific row with a specific council_area
            counter = 0
            for col in dataset_encoded.columns:
                if counter == index:
                    list_metrics.append(col)
                counter = counter+1

        i = i+1

    counterlist = Counter(list_metrics)
    # Return the most common metric in the list of metrics
    return counterlist.most_common

