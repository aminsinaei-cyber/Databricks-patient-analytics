-- Compare hospital revenue and profit using two separate horizontal bar charts: Revenue by Hospital and Profit by Hospital.

SELECT hospital,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS record_count
FROM patient_analytics
GROUP BY hospital
ORDER BY total_revenue DESC;
