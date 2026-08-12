-- ============================================
-- TASK 2: SQL BUSINESS ANALYSIS
-- ============================================

-- Q1. Top 5 Products by Total Revenue
SELECT
    Product,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Q2. Revenue by Product Category
SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;


-- Q3. What is the monthly sales trend?
SELECT
    Order_Year,
    Order_Month,
    ROUND(SUM(Total_Sales), 2) AS Monthly_Sales
FROM sales
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;

-- Q4. Top 5 Cities by Revenue
SELECT
    City,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY City
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Q5. Revenue by Age Group
SELECT
    Age_Group,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY Age_Group
ORDER BY Total_Revenue DESC;


-- Q6. Sales by Gender
SELECT
    Gender,
    COUNT(*) AS Number_of_Orders,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY Gender
ORDER BY Total_Revenue DESC;


-- Q7. Top 10 Customers by Revenue
SELECT
    Customer_ID,
    Customer_Name,
    COUNT(Order_ID) AS Number_of_Orders,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Revenue DESC
LIMIT 10;


-- Q8. Top customers using a multi-table JOIN

SELECT
    s.Customer_ID,
    c.Customer_Name,
    c.City,
    COUNT(s.Order_ID) AS Number_of_Orders,
    ROUND(SUM(s.Total_Sales), 2) AS Total_Revenue
FROM sales AS s
INNER JOIN customers AS c
    ON s.Customer_ID = c.Customer_ID
GROUP BY
    s.Customer_ID,
    c.Customer_Name,
    c.City
ORDER BY Total_Revenue DESC
LIMIT 10;