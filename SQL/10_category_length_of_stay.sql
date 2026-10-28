-- Compare average length of stay by service category using a horizontal bar chart.

SELECT category,
       ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay,
       COUNT(*) AS service_records
FROM patient_analytics
GROUP BY category
ORDER BY avg_length_of_stay DESC;
