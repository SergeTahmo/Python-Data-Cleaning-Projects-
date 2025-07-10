
"""
This repository contains a collection of Python scripts and Jupyter Notebooks
for cleaning and preprocessing data before analysis or modeling.

It includes missing value treatment, outlier detection, duplicate removal,
data type conversion, and Exploratory Data Analysis (EDA).
"""

# === Folder Structure ===
# data-cleaning-scripts/
# ├── missing_values/
# │   └── handle_missing_values.ipynb
# ├── duplicates_handling/
# │   └── remove_duplicates.ipynb
# ├── outlier_detection/
# │   └── detect_outliers_zscore.py
# ├── eda_visualization/
# │   └── eda_titanic.ipynb
# ├── utils/
# │   └── data_loader.py
# ├── datasets/
# │   ├── titanic.csv
# │   └── nyc_311_data_sample.csv
# └── README.md

# === Sample: handle_missing_values.ipynb ===

import pandas as pd

# Load dataset
df = pd.read_csv('../datasets/titanic.csv')

# Summary of missing data
print(df.isnull().sum())

# Fill missing age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop rows where Embarked is missing
df.dropna(subset=['Embarked'], inplace=True)

# Replace missing Cabin with 'Unknown'
df['Cabin'].fillna('Unknown', inplace=True)

# Save cleaned data
df.to_csv('../datasets/titanic_cleaned.csv', index=False)

# === Sample: remove_duplicates.ipynb ===

# Check for duplicates
print("Duplicate Rows:", df.duplicated().sum())

# Drop duplicate rows
df_cleaned = df.drop_duplicates()

# Save output
df_cleaned.to_csv('../datasets/titanic_no_duplicates.csv', index=False)

# === detect_outliers_zscore.py ===

import numpy as np

def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(x - mean) / std for x in data]
    return [x for x, z in zip(data, z_scores) if abs(z) > threshold]

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('../datasets/titanic.csv')
    fare_outliers = detect_outliers_zscore(df['Fare'].dropna())
    print(f"Detected outliers in Fare: {fare_outliers[:5]}")

# === eda_titanic.ipynb ===

import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('../datasets/titanic_cleaned.csv')

# Distribution of Age
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Survival rate by class
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()

# === data_loader.py ===

def load_data(filepath):
    import pandas as pd
    return pd.read_csv(filepath)

# === README.md ===

"""
# Data Cleaning & Preprocessing Scripts

This repository includes Python scripts and notebooks for essential data cleaning tasks:

## 🧹 Main Topics
- Handling Missing Values
- Removing Duplicates
- Outlier Detection (Z-score)
- Exploratory Data Analysis (EDA)

## Datasets Used
- Titanic Dataset (Kaggle)
- NYC 311 Complaints (Open Data)

## 🛠 Tools
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Example Visuals
- Histogram of Age Distribution
- Survival Rate by Passenger Class

## How to Use
Clone the repo and explore individual folders:
```bash
cd missing_values
jupyter notebook handle_missing_values.ipynb
```

---

Contributions welcome. Happy cleaning!
"""
