-- Four KPI counters: Total Revenue, Reported Profit, Unique Patients, and Average Length of Stay. The distinct patient count differs from the record count.

SELECT ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(DISTINCT patient_id) AS unique_patients,
       ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay
FROM patient_analytics;
