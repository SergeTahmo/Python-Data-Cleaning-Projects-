## Titanic Data Cleaning & Preprocessing Script

This Python script performs essential data cleaning and preprocessing steps on the Titanic dataset,
commonly used for data science tutorials and predictive modeling.

Key Features:
- **Missing Value Treatment**:
    - Fills missing `Age` with median.
    - Replaces missing `Embarked` with mode.
    - Substitutes missing `Cabin` values with "Unknown".

- **Duplicate Handling**:
    - Identifies and removes duplicate records to ensure data consistency.

- **Outlier Detection**:
    - Detects outliers in the `Fare` column using the Z-score method for potential anomaly handling.

- **Exploratory Data Analysis (EDA)**:
    - Visualizes age distribution, survival rates by passenger class, and gender-based survival.

- **Data Export**:
    - Saves the cleaned dataset to `titanic_cleaned.csv` for further analysis or modeling.

 Dependencies:
- pandas
- numpy
- matplotlib
- seaborn

Ideal for:
- Beginners practicing data cleaning workflows
- Data scientists preparing Titanic data for ML models
- Analysts performing exploratory visualizations
