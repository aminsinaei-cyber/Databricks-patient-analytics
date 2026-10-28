-- Calculate average, minimum, and maximum length of stay and record counts by hospital; displayed as a horizontal bar chart.

SELECT hospital,
       ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay,
       MIN(length_of_stay) AS min_length_of_stay,
       MAX(length_of_stay) AS max_length_of_stay,
       COUNT(*) AS service_records
FROM patient_analytics
GROUP BY hospital
ORDER BY avg_length_of_stay DESC;
