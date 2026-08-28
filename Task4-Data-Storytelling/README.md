# 📊 Task 4 — Data Storytelling & Statistical Validation

## Project Title
**Sales Analytics: From Raw Data to Business Decisions**

## Overview
This project is part of my Data Analytics Internship and focuses on transforming analytical findings into a clear business story and validating key insights using statistical methods.

The project combines insights from data cleaning, exploratory data analysis, SQL analysis, customer segmentation, Power BI dashboarding, and hypothesis testing to generate actionable business recommendations.

---

## Business Objective
The objective of this project is to analyze sales and customer data to:

- Understand overall revenue performance
- Identify high-value customer segments
- Analyze product and geographic performance
- Study monthly sales trends
- Validate business assumptions statistically
- Provide actionable recommendations for business growth

---

## Key Business KPIs

| KPI | Value |
|---|---:|
| Total Revenue | ₹13.94 Cr |
| Total Orders | 1,000 |
| Average Order Value | ₹139K |
| Total Customers | 947 |
| Revenue per Customer | ₹147K |

---

## Key Business Insights

### Customer Segmentation
- High Value Customers: **316**
- Revenue Contribution: **66.3%**
- Medium Value Customers: **315**
- Revenue Contribution: **26.3%**
- Low Value Customers: **316**
- Revenue Contribution: **7.4%**

**Main Insight:**  
Nearly one-third of customers generate approximately two-thirds of total revenue.

---

### Product Performance

Top revenue-generating products:

1. Laptop — ₹2.54 Cr
2. Mobile — ₹2.53 Cr
3. Book — ₹2.50 Cr
4. Rice — ₹2.22 Cr
5. Chair — ₹2.15 Cr

Electronics emerged as the highest revenue-generating category.

---

### Geographic Performance

Top-performing cities include:

- Patna
- Kolkata
- Bengaluru
- Mumbai
- Hyderabad

Patna generated the highest revenue among the analyzed cities.

---

## Statistical Validation

### Business Question
Does customer gender have a statistically significant impact on average order sales?

### Hypotheses

**H₀ — Null Hypothesis:**  
There is no statistically significant difference in average order sales between male and female customers.

**H₁ — Alternative Hypothesis:**  
There is a statistically significant difference in average order sales between male and female customers.

### Test Used
**Welch’s Independent Samples T-Test**

### Statistical Results

| Metric | Result |
|---|---:|
| Male Orders | 511 |
| Female Orders | 489 |
| Male Average Sales | ₹141,807.34 |
| Female Average Sales | ₹136,883.21 |
| T-Statistic | 0.6826 |
| P-Value | 0.4950 |
| Significance Level | 0.05 |
| Decision | Fail to Reject H₀ |

### Conclusion

Since the p-value (**0.4950**) is greater than the significance level (**0.05**), the null hypothesis was not rejected.

The analysis indicates that gender alone is not a statistically significant driver of average customer spending.

---

## Business Recommendations

- Retain High Value customers using loyalty and personalized engagement strategies
- Convert Medium Value customers into High Value customers through targeted promotions
- Prioritize high-performing products and categories
- Focus regional strategies on high-performing cities
- Use behavioral and value-based customer segmentation instead of primarily gender-based targeting

---

## Presentation

The final stakeholder presentation summarizes the complete business story including:

- Business Objective
- Analytics Journey
- Executive KPIs
- Product & Geographic Performance
- Customer Segmentation
- Power BI Dashboard Insights
- Statistical Validation
- Strategic Recommendations

The presentation is designed for a **7–10 minute stakeholder presentation**.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- SQL
- Microsoft Power BI
- DAX
- Jupyter Notebook
- Git & GitHub

---

## Project Structure

```text
Task4-Data-Storytelling/
│
├── task3_dashboard_data.csv
├── task4_hypothesis_testing.ipynb
├── hypothesis_testing_summary.md
├── data_story.md
├── Final_Sales_Analytics_Presentation.pptx
└── README.md