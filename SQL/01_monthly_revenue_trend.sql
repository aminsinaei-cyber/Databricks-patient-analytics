-- Analyze monthly total revenue, reported profit, and record count using a line chart with admission_month on the X-axis.

SELECT admission_month,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS record_count
FROM patient_analytics
GROUP BY admission_month
ORDER BY admission_month;
