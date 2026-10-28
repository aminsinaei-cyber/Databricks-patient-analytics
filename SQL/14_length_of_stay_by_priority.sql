-- Compare average length of stay by admission priority; the horizontal bar chart uses avg_length_of_stay, not record_count.

SELECT priority,
       ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay,
       COUNT(*) AS record_count
FROM patient_analytics
GROUP BY priority
ORDER BY avg_length_of_stay DESC;
