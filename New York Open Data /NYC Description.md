## 🗽 NYC 311 Service Requests – Data Cleaning & Preprocessing

This project focuses on cleaning and preprocessing a sample dataset of 311 service requests in New York City. The data originates from NYC Open Data and contains records of complaints reported by residents to various city departments.

### 🎯 Objective
To transform raw, messy real-world data into a structured and analysis-ready format by applying robust cleaning techniques. This cleaned dataset can be used for:
- Public service analysis
- Complaint distribution mapping
- Time series and trend analysis
- Operational reporting

---

### 🔧 Key Cleaning Steps

1. **Initial Data Inspection**  
   - Assess missing values and understand the overall structure and schema.

2. **Column Pruning**  
   - Drop irrelevant and redundant columns (e.g., school and park-related fields, intersections).

3. **Missing Value Treatment**  
   - Drop rows where `Complaint Type` or `Borough` is missing (essential for analysis).
   - Fill missing `Descriptor` fields with `"Unknown"`.

4. **Date Parsing & Feature Engineering**  
   - Convert the `Created Date` column to proper datetime format.
   - Extract `Year`, `Month`, and `Day of the Week` for trend analysis.

5. **Duplicate Removal**  
   - Identify and remove exact duplicate complaint records.

6. **Final Output**  
   - Export cleaned data to `datasets/nyc_311_cleaned.csv`.

---

### 🛠 Tools & Technologies
- **Language**: Python  
- **Libraries**: `pandas`, `numpy`

---

### 📁 Input Dataset
- `nyc_311_data_sample.csv`: A raw dataset containing a sample of NYC 311 complaint records.

### 📁 Output Dataset
- `nyc_311_cleaned.csv`: The cleaned, transformed version ready for analysis or visualization.

---

### ✅ Use Cases Post-Cleaning
- Identify top complaint types by borough
- Analyze complaint trends over time
- Visualize complaint frequency by weekday
- Support public service planning & performance tracking

---

### 📌 Dataset Source
Data is based on NYC Open Data's 311 Service Requests:  
[https://data.cityofnewyork.us/Social-Services/311-Service-Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests)

---

### 📤 How to Run

```bash
python nyc311_data_cleaning.py
