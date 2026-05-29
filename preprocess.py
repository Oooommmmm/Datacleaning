import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = "data.csv"  
OUTPUT_FILENAME = "cleaned_dataset.csv"  

df = pd.read_csv(DATA_PATH)

true_num_cols = ["Age", "Fare", "SibSp", "Parch"]
exclude_cols = ["PassengerId", "Survived", "Pclass"]
cat_cols = [
    col
    for col in df.columns
    if col not in true_num_cols + exclude_cols and df[col].dtype == "object"
]

for col in true_num_cols:
    if col in df.columns and df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    if df[col].isnull().sum() > 0:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

df_encoded = df.copy()

if cat_cols:
    encoder = OneHotEncoder(sparse_output=False, drop="first")
    encoded_features = encoder.fit_transform(df_encoded[cat_cols])
    encoded_df = pd.DataFrame(
        encoded_features, columns=encoder.get_feature_names_out(cat_cols)
    )
    df_encoded = pd.concat([df_encoded.drop(columns=cat_cols), encoded_df], axis=1)

plt.figure(figsize=(10, 5))
sns.boxplot(data=df_encoded[true_num_cols])
plt.title("Before Outlier Removal")
plt.tight_layout()
plt.show()

for col in true_num_cols:
    if col in df_encoded.columns:
        Q1 = df_encoded[col].quantile(0.25)
        Q3 = df_encoded[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df_encoded = df_encoded[
            (df_encoded[col] >= lower_bound) & (df_encoded[col] <= upper_bound)
        ]

plt.figure(figsize=(10, 5))
sns.boxplot(data=df_encoded[true_num_cols])
plt.title("After Outlier Removal")
plt.tight_layout()
plt.show()

scaler = StandardScaler()
df_encoded[true_num_cols] = scaler.fit_transform(df_encoded[true_num_cols])

df_encoded.to_csv(OUTPUT_FILENAME, index=False)

print("cleaning done")