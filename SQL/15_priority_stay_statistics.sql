-- Calculate average, median, 95th percentile, and maximum length of stay to investigate differences in the Low-priority group; grouped columns compare average and median.

SELECT priority,
       COUNT(*) AS record_count,
       ROUND(AVG(length_of_stay), 2) AS avg_stay,
       PERCENTILE_APPROX(length_of_stay, 0.5) AS median_stay,
       PERCENTILE_APPROX(length_of_stay, 0.95) AS p95_stay,
       MAX(length_of_stay) AS max_stay
FROM patient_analytics
GROUP BY priority
ORDER BY avg_stay DESC;
