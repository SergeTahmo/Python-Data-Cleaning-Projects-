"""
 Script: nyc311_data_cleaning.py

NYC 311 Complaints Data Cleaning & Preprocessing Script

This script performs data cleaning on a sample of NYC 311 Service Request data.
It prepares the data for analysis by addressing missing values, removing duplicates,
converting data types, and engineering useful features.

Key Steps:
- Drops irrelevant columns
- Handles missing values in key complaint fields
- Parses dates and extracts year, month, and weekday
- Removes duplicate records
- Saves cleaned dataset for analysis

 Libraries Used:
- pandas
- numpy
"""

import pandas as pd
import numpy as np

# === Load Raw Data ===
df = pd.read_csv("datasets/nyc_311_data_sample.csv")

print("\n Initial Inspection")
print("Rows, Columns:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# === Drop Irrelevant Columns ===
columns_to_drop = [
    "Unnamed: 0",
    "Intersection Street 1",
    "Intersection Street 2",
    "Park Facility Name",
    "Park Borough",
    "School Name",
    "School Number",
    "School Region",
    "School Code",
    "School Phone Number",
    "School Address"
]

df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# === Handle Missing Values ===
df.dropna(subset=["Complaint Type", "Borough"], inplace=True)
df["Descriptor"].fillna("Unknown", inplace=True)

# === Convert and Parse Dates ===
df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
df = df[df["Created Date"].notnull()]  # Remove rows with invalid or missing dates

# === Feature Engineering ===
df["Year"] = df["Created Date"].dt.year
df["Month"] = df["Created Date"].dt.month
df["DayOfWeek"] = df["Created Date"].dt.day_name()

# === Remove Duplicates ===
print("Duplicates Found:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# === Sample Output Preview ===
print("\n Cleaned Sample Preview:")
print(df.head(3))

# === Save Cleaned Dataset ===
output_path = "datasets/nyc_311_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\n Cleaned NYC 311 data saved to: {output_path}")
