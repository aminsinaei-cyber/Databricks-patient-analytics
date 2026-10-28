-- Compare revenue and profit across payor groups using two horizontal bar charts.

SELECT payor_segment,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS service_records,
       COUNT(DISTINCT patient_id) AS unique_patients
FROM patient_analytics
GROUP BY payor_segment
ORDER BY total_revenue DESC;
