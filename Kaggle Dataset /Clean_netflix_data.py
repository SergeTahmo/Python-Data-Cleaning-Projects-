"""
📂 Script: clean_netflix_data.py

🧹 Netflix Movies and TV Shows – Data Cleaning Script

This script cleans the Netflix metadata dataset from Kaggle. It handles missing values,
fixes data types, and extracts new features like release year, added month, and content type breakdown.

🔍 Key Steps:
- Handle missing values (director, cast, country)
- Convert 'date_added' to datetime
- Extract new features: year_added, month_added
- Remove duplicates
- Export cleaned dataset

📦 Libraries Used:
- pandas
- numpy
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("datasets/netflix_titles.csv")

print("\n Initial Overview")
print("Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# === Handle Missing Values ===
# Fill missing Director and Cast with 'Unknown'
df["director"].fillna("Unknown", inplace=True)
df["cast"].fillna("Unknown", inplace=True)

# Fill missing country with mode
df["country"].fillna(df["country"].mode()[0], inplace=True)

# Drop rows where 'date_added' or 'title' is missing
df.dropna(subset=["date_added", "title"], inplace=True)

# === Convert Date Fields ===
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract Year and Month of addition to Netflix
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

# === Feature Engineering ===
# Create binary flags for content type
df["is_movie"] = df["type"].apply(lambda x: 1 if x == "Movie" else 0)
df["is_tv_show"] = df["type"].apply(lambda x: 1 if x == "TV Show" else 0)

# === Remove Duplicates ===
print("Duplicates Found:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# === Export Cleaned Dataset ===
output_path = "datasets/netflix_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Cleaned Netflix dataset saved to: {output_path}")
