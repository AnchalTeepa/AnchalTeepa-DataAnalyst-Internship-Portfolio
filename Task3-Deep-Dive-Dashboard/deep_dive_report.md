# Task 3 — Deep-Dive Analysis & Interactive Dashboarding

## Project Overview

This project focuses on performing a detailed analysis of sales data to identify customer behavior, revenue patterns, product performance, and geographic trends.

The analysis was conducted using Python for exploratory and deep-dive analysis, while Power BI was used to develop an interactive business intelligence dashboard for monitoring key performance indicators and business trends.

---

## Business Objective

The primary objectives of this analysis are to:

- Evaluate overall sales and revenue performance.
- Identify high-value, medium-value, and low-value customers.
- Analyze customer contribution to total business revenue.
- Identify top-performing products.
- Analyze revenue performance across cities and business segments.
- Understand monthly revenue trends.
- Develop an interactive dashboard for business decision-making.

---

## Dataset Overview

The cleaned sales dataset contains transactional information including:

- Order ID
- Order Date
- Customer ID
- Product
- Category
- Quantity
- Total Sales
- City
- Customer Segment

The cleaned dataset was further analyzed and transformed to support customer segmentation and interactive dashboard development.

---

## Core KPIs

| KPI | Value | Business Purpose |
|---|---:|---|
| Total Revenue | ₹13.94 Cr | Measures overall business revenue |
| Total Orders | 1K | Measures total customer orders |
| Average Order Value | ₹139K | Measures average revenue generated per order |
| Total Customers | 947 | Measures the active customer base |
| Revenue per Customer | ₹147K | Measures average revenue generated per customer |

---

## Customer Segmentation Analysis

Customers were classified into three groups based on their total revenue contribution:

| Customer Segment | Customers | Revenue | Revenue Share |
|---|---:|---:|---:|
| High Value | 316 | ₹9.24 Cr | 66.3% |
| Medium Value | 315 | ₹3.67 Cr | 26.3% |
| Low Value | 316 | ₹1.04 Cr | 7.4% |

### Key Finding

High-value customers generate approximately **66.3% of total revenue**, despite representing roughly one-third of the customer base.

This indicates that customer retention and personalized engagement strategies for high-value customers can have a significant impact on overall business performance.

---

## Sales Trend Analysis

Monthly revenue analysis was performed to understand changes in business performance over time.

The interactive dashboard allows users to evaluate revenue trends across the available reporting period and dynamically analyze performance using date filters.

Monitoring monthly revenue patterns can help businesses identify:

- Strong and weak sales periods
- Revenue fluctuations
- Seasonal patterns
- Potential opportunities for targeted campaigns

---

## Product Performance Analysis

Product-level revenue analysis was conducted to identify the highest-performing products.

The dashboard includes a **Top Products by Revenue** visualization, enabling decision-makers to quickly identify products contributing strongly to overall sales.

### Business Use

Top-performing products can be prioritized for:

- Inventory planning
- Marketing campaigns
- Product promotions
- Cross-selling opportunities

Products with comparatively weaker performance can be further investigated to identify pricing, demand, or positioning issues.

---

## Geographic Analysis

Revenue was analyzed across different cities to identify geographically strong markets.

The dashboard includes a **Top Cities by Revenue** visualization to highlight locations generating the highest business revenue.

### Business Use

Geographic performance analysis can support:

- Regional marketing strategies
- Sales resource allocation
- Inventory distribution
- Market expansion decisions

---

## Business Segment Analysis

Revenue performance was also evaluated across available business/customer segments.

Segment-level analysis provides an additional perspective on how different customer groups contribute to overall business performance.

This information can help organizations develop targeted marketing and customer engagement strategies.

---

## Interactive Power BI Dashboard

A professional interactive dashboard was developed in Microsoft Power BI.

### Dashboard Features

- Date Range filter
- Category filter
- Customer Segment filter
- City filter
- Reset Filters button
- Total Revenue KPI
- Total Orders KPI
- Average Order Value KPI
- Total Customers KPI
- Revenue per Customer KPI
- Monthly Revenue Trend
- Revenue by Customer Segment
- Top Products analysis
- Top Cities analysis
- Customer Segment Summary

All major dashboard visuals respond dynamically to user selections, allowing users to perform interactive business analysis.

---

## Key Business Insights

1. Total business revenue reached approximately **₹13.94 Cr**.

2. The dataset contains approximately **1,000 orders from 947 customers**.

3. High-value customers contribute approximately **66.3% of total revenue**, making them the most commercially important customer group.

4. Medium-value customers contribute approximately **26.3% of revenue**, representing an important opportunity for conversion into high-value customers.

5. Low-value customers contribute approximately **7.4% of total revenue**, despite representing a similar number of customers.

6. Product-level analysis identifies the products responsible for the largest revenue contribution.

7. Geographic analysis highlights the strongest revenue-generating cities.

8. Monthly revenue monitoring provides visibility into sales fluctuations and changing business performance.

---

## Business Recommendations

### 1. Retain High-Value Customers
Develop loyalty programs, personalized offers, and targeted communication for high-value customers.

### 2. Grow Medium-Value Customers
Use cross-selling, upselling, and personalized recommendations to increase spending among medium-value customers.

### 3. Improve Low-Value Customer Engagement
Analyze purchase behavior and introduce targeted promotions to improve engagement and repeat purchases.

### 4. Prioritize Top Products
Maintain adequate inventory and increase promotional efforts for consistently high-performing products.

### 5. Optimize Geographic Strategy
Allocate marketing and sales resources toward high-performing cities while investigating growth opportunities in weaker markets.

### 6. Continuously Monitor KPIs
Use the interactive Power BI dashboard to regularly monitor revenue, orders, customer behavior, and sales trends.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Microsoft Power BI
- DAX
- CSV
- Git
- GitHub

---

## Conclusion

The project demonstrates how transactional sales data can be transformed into meaningful business insights through deep-dive analysis and interactive dashboarding.

Customer segmentation revealed a strong concentration of revenue among high-value customers, while product, geographic, and time-based analysis provided additional perspectives on business performance.

The Power BI dashboard converts these analytical findings into an interactive decision-support tool that enables stakeholders to monitor KPIs, explore trends, and make more informed business decisions.