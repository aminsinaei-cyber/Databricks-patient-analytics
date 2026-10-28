-- Compare revenue and profit by region using two horizontal bar charts, along with record count, distinct patient count, and average length of stay.

SELECT region,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS service_records,
       COUNT(DISTINCT patient_id) AS unique_patients,
       ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay
FROM patient_analytics
GROUP BY region
ORDER BY total_revenue DESC;
