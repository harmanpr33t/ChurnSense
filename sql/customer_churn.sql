CREATE DATABASE ChurnSense;

USE ChurnSense;

SELECT *
FROM customers;

SELECT COUNT(*)
FROM customers;

SELECT Churn,
COUNT(*)
FROM customers
GROUP BY Churn;

SELECT Gender,
COUNT(*)
FROM customers
GROUP BY Gender;

SELECT Contract,
COUNT(*)
FROM customers
GROUP BY Contract;

SELECT PaymentMethod,
COUNT(*)
FROM customers
GROUP BY PaymentMethod;

SELECT AVG(MonthlyCharges)
FROM customers;

SELECT MAX(MonthlyCharges)
FROM customers;

SELECT MIN(MonthlyCharges)
FROM customers;

SELECT InternetService,
AVG(MonthlyCharges)
FROM customers
GROUP BY InternetService;

SELECT Contract,
AVG(Tenure)
FROM customers
GROUP BY Contract;

SELECT Churn,
AVG(Tenure)
FROM customers
GROUP BY Churn;

SELECT Churn,
AVG(MonthlyCharges)
FROM customers
GROUP BY Churn;

SELECT Contract,
COUNT(*)
FROM customers
WHERE Churn='Yes'
GROUP BY Contract;

SELECT PaymentMethod,
COUNT(*)
FROM customers
WHERE Churn='Yes'
GROUP BY PaymentMethod;