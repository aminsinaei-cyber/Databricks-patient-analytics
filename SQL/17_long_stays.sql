-- Examine the number and maximum duration of long stays by priority. The Low-priority group had seven records exceeding 10 days.

SELECT priority,
       COUNT(*) AS long_stay_records,
       MAX(length_of_stay) AS max_stay
FROM patient_analytics
WHERE length_of_stay > 10
GROUP BY priority
ORDER BY long_stay_records DESC;
