-- Scatter plot: X = length_of_stay, Y = revenue, color = hospital. Each point represents one record.

SELECT length_of_stay, revenue, hospital, priority
FROM patient_analytics
WHERE revenue IS NOT NULL
  AND length_of_stay IS NOT NULL;
