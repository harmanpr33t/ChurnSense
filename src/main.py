import os
import pandas as pd
from preprocessing import preprocess_data
from train_model import train_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "dataset", "churn_data.csv")

print("=" * 60)
print("         CHURNSENSE")
print("=" * 60)

if not os.path.exists(DATA_PATH):
    print("Dataset Not Found")
    exit()

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

X_train, X_test, y_train, y_test, feature_names = preprocess_data(df)

accuracy, report, matrix, importance = train_model(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names
)

print("\nAccuracy")
print(accuracy)

print("\nConfusion Matrix")
print(matrix)

print("\nClassification Report")
print(report)

print("\nTop Features")
print(importance.head(10))

print("\nProject Executed Successfully")