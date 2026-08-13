"""
ApexPlanet Data Analytics Internship — Task 1
Data Immersion & Wrangling
"""

from pathlib import Path

import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUT_CSV = BASE_DIR / "cleaned_sales_data.csv"
OUT_XLSX = BASE_DIR / "cleaned_sales_data.xlsx"
REPORT_PATH = BASE_DIR / "data_quality_report.txt"

report_lines = []

def log(msg=""):
    print(msg)
    report_lines.append(str(msg))

# 1. LOAD & PROFILE
log("=" * 70)
log("APEXPLANET SALES DATASET — DATA QUALITY REPORT")
log("=" * 70)

df = pd.read_excel(RAW_PATH, sheet_name="Sales_Dataset")
log(f"\nRaw shape: {df.shape[0]} rows x {df.shape[1]} columns")
log("\n--- Missing values (raw) ---")
log(df.isnull().sum().to_string())

dup_ids = df[df["Order_ID"].duplicated(keep=False)].sort_values("Order_ID")
log(f"\nRows sharing a duplicated Order_ID: {len(dup_ids)}")

# 2. CLEANING
text_cols = df.select_dtypes(include="object").columns.tolist()
for c in text_cols:
    df[c] = df[c].astype("string").str.strip()

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

df["Is_Duplicate_ID_Fixed"] = False
dupe_mask = df["Order_ID"].duplicated(keep=False)
counters = {}
new_ids = df["Order_ID"].copy()
for idx in df[dupe_mask].index:
    oid = df.at[idx, "Order_ID"]
    counters[oid] = counters.get(oid, 0) + 1
    if counters[oid] > 1:
        new_ids.at[idx] = f"{oid}-{counters[oid]}"
        df.at[idx, "Is_Duplicate_ID_Fixed"] = True
df["Order_ID"] = new_ids
log(f"\nOrder_IDs re-keyed to restore uniqueness: {df['Is_Duplicate_ID_Fixed'].sum()}")

df["Age_Imputed"] = df["Age"].isna()
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age).astype(int)
log(f"Age missing values imputed with median ({median_age:.0f}): {df['Age_Imputed'].sum()}")

df["City_Imputed"] = df["City"].isna()
df["City"] = df["City"].fillna("Unknown")
log(f"City missing values labeled 'Unknown': {df['City_Imputed'].sum()}")

for c in ["Gender", "City", "Product", "Category"]:
    df[c] = df[c].astype("category")

# 3. FEATURE ENGINEERING
bins = [17, 25, 35, 45, 55, 65]
labels = ["18-25", "26-35", "36-45", "46-55", "56-65"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)

df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month_name()
df["Order_Weekday"] = df["Order_Date"].dt.day_name()
df["Order_Quarter"] = df["Order_Date"].dt.quarter

q1, q3 = df["Total_Sales"].quantile([0.25, 0.75])
iqr = q3 - q1
low_fence, high_fence = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["Is_Sales_Outlier"] = (df["Total_Sales"] < low_fence) | (df["Total_Sales"] > high_fence)
log(f"\nTotal_Sales statistical outliers flagged: {df['Is_Sales_Outlier'].sum()}")

ordered_cols = [
    "Order_ID", "Order_Date", "Order_Year", "Order_Month", "Order_Quarter", "Order_Weekday",
    "Customer_ID", "Customer_Name", "Age", "Age_Group", "Gender", "City",
    "Product", "Category", "Quantity", "Unit_Price", "Total_Sales",
    "Is_Sales_Outlier", "Age_Imputed", "City_Imputed", "Is_Duplicate_ID_Fixed",
]
df = df[ordered_cols]

# 4. VALIDATION
log("\n--- Post-cleaning missing values ---")
log(df.isnull().sum().to_string())
log(f"\nFinal shape: {df.shape[0]} rows x {df.shape[1]} columns")

# 5. EXPORT
df.to_csv(OUT_CSV, index=False)
df.to_excel(OUT_XLSX, index=False, sheet_name="Cleaned_Sales")

with open(REPORT_PATH, "w") as f:
    f.write("\n".join(report_lines))

log(f"\nSaved -> {OUT_CSV}, {OUT_XLSX}, {REPORT_PATH}")