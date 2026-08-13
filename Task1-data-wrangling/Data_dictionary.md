# Data Dictionary — ApexPlanet Sales Dataset (Cleaned)

**Prepared by:** Anchal Teepa
**Date:** 5 Aug 2026
**Source file:** ApexPlanet_DataAnalytics_Dataset.xlsx (sheet: Sales_Dataset)
**Cleaned output:** cleaned_sales_data.csv / cleaned_sales_data.xlsx
**Grain:** one row = one order line item
**Row count:** 1,000 (no rows were dropped during cleaning)

| # | Column | Type | Description | Business Relevance |
|---|--------|------|--------------|---------------------|
| 1 | Order_ID | string | Unique order identifier. 8 IDs were re-keyed during cleaning to remove duplicates. | Primary key for joining orders across tables/tasks. |
| 2 | Order_Date | date | Date the order was placed. | Basis for all time-series and trend analysis. |
| 3 | Order_Year | int | Year extracted from Order_Date. (engineered) | Year-over-year comparisons. |
| 4 | Order_Month | string | Month name extracted from Order_Date. (engineered) | Seasonality analysis. |
| 5 | Order_Quarter | int (1-4) | Calendar quarter. (engineered) | Quarterly business reporting. |
| 6 | Order_Weekday | string | Day of week the order was placed. (engineered) | Identifies weekday vs. weekend buying patterns. |
| 7 | Customer_ID | string | Unique customer identifier. | Links repeat orders to the same customer; basis for cohort/retention analysis (Task 3). |
| 8 | Customer_Name | string | Customer's full name. | Display/reporting only — not used for analysis (PII). |
| 9 | Age | int | Customer age in years. 20 missing values imputed with the dataset median (41). | Demographic segmentation. |
| 10 | Age_Group | category | Age bucketed into 5 bands (18-25, 26-35, 36-45, 46-55, 56-65). (engineered) | Simplifies age-based segmentation for dashboards. |
| 11 | Gender | category | Customer gender (Male/Female). | Demographic segmentation. |
| 12 | City | category | Customer's city (8 Indian cities). 13 missing values labeled "Unknown". | Geographic/regional sales analysis. |
| 13 | Product | category | Product purchased (6 distinct products). | Product-level performance analysis. |
| 14 | Category | category | Product category (Grocery, Education, Electronics, Fashion, Furniture). | Category-level performance analysis. |
| 15 | Quantity | int | Units purchased in this order line (1-10). | Volume analysis, demand forecasting. |
| 16 | Unit_Price | float | Price per unit (₹). | Pricing analysis. |
| 17 | Total_Sales | float | Revenue for the line item. Verified equal to Quantity × Unit_Price for all 1,000 rows. | Core revenue metric — basis for all KPIs. |
| 18 | Is_Sales_Outlier | boolean | True if Total_Sales falls outside the IQR fence. (engineered) | Lets analysts include/exclude high-value orders without deleting data. |
| 19 | Age_Imputed | boolean | True if Age was originally missing and filled with the median. (engineered) | Data-quality transparency/auditability. |
| 20 | City_Imputed | boolean | True if City was originally missing and labeled "Unknown". (engineered) | Data-quality transparency/auditability. |
| 21 | Is_Duplicate_ID_Fixed | boolean | True if this row's Order_ID was re-keyed because it originally collided with other rows. (engineered) | Data-quality transparency/auditability. |

---

## Data Quality Issues Found & How They Were Resolved

| Issue | Rows Affected | Resolution | Rationale |
|---|---|---|---|
| Missing Age | 20 (2.0%) | Imputed with dataset median (41) | Median is robust to outliers/skew; a flag column preserves transparency. |
| Missing City | 13 (1.3%) | Labeled "Unknown" | Avoids fabricating a customer's location; keeps the row usable in aggregate metrics. |
| Duplicate Order_ID | 9 rows sharing "ORD100050" (8 collisions) | Re-keyed to "ORD100050-2" … "ORD100050-9", original preserved | Rows are not true duplicates (different customers/dates/amounts) — this is a key-generation error, not a repeated transaction, so no rows were dropped. |
| Total_Sales formula check | 0 mismatches | No action needed | Confirms revenue field is internally consistent and trustworthy. |
| Statistical outliers in Total_Sales | 19 (1.9%) | Flagged, not removed | High-value orders are legitimate (Unit_Price ranges from ₹146 to ₹49,998). |

No fully duplicated rows were found. No malformed date strings were found.