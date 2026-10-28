-- Count records and distinct patients by admission priority; use record_count for the donut chart.

SELECT priority,
       COUNT(*) AS record_count,
       COUNT(DISTINCT patient_id) AS unique_patients
FROM patient_analytics
GROUP BY priority
ORDER BY record_count DESC;
