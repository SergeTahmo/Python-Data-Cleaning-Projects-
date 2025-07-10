Titanic Data Cleaning & Preprocessing Script

This Python script performs essential data cleaning and preprocessing steps on the Titanic dataset,
commonly used for data science tutorials and predictive modeling.

 Key Features:
- Missing Value Treatment
- Duplicate Removal
- Outlier Detection (Z-score)
- Exploratory Data Analysis (EDA) Visualizations
- Cleaned Dataset Export

 Dependencies:
- pandas
- numpy
- matplotlib
- seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# Step 1: Load the Dataset
# ==========================
df = pd.read_csv("datasets/titanic.csv")

print(" Initial Data Overview:")
print("Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())
print("Data Types:\n", df.dtypes)

# ==========================
# Step 2: Handle Missing Values
# ==========================
# Fill missing Age values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked values with the mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Replace missing Cabin values with 'Unknown'
df['Cabin'].fillna("Unknown", inplace=True)

# ==========================
# Step 3: Remove Duplicates
# ==========================
duplicates = df.duplicated().sum()
print(f"\n🧹 Duplicate Rows Found: {duplicates}")
df.drop_duplicates(inplace=True)

# ==========================
# Step 4: Outlier Detection (Fare column)
# ==========================
def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(x - mean) / std for x in data]
    return [x for x, z in zip(data, z_scores) if abs(z) > threshold]

fare_outliers = detect_outliers_zscore(df['Fare'].dropna())
print(f"\n🚨 Fare Outliers Detected (sample): {fare_outliers[:5]}")

# ==========================
# Step 5: Exploratory Data Analysis
# ==========================
print("\n📈 Generating Visuals...")

# Age Distribution
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Survival Rate by Passenger Class
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.show()

# Gender-based Survival
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ==========================
# Step 6: Export Cleaned Data
# ==========================
output_path = "datasets/titanic_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\n Cleaned dataset saved to: {output_path}")
