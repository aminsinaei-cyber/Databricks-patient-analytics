-- Count records within length-of-stay ranges; order the column chart by sort_order rather than record count.

SELECT
    CASE
        WHEN length_of_stay = 0 THEN '0 days'
        WHEN length_of_stay = 1 THEN '1 day'
        WHEN length_of_stay = 2 THEN '2 days'
        WHEN length_of_stay BETWEEN 3 AND 5 THEN '3-5 days'
        WHEN length_of_stay BETWEEN 6 AND 10 THEN '6-10 days'
        ELSE '11+ days'
    END AS stay_group,
    CASE
        WHEN length_of_stay = 0 THEN 1
        WHEN length_of_stay = 1 THEN 2
        WHEN length_of_stay = 2 THEN 3
        WHEN length_of_stay BETWEEN 3 AND 5 THEN 4
        WHEN length_of_stay BETWEEN 6 AND 10 THEN 5
        ELSE 6
    END AS sort_order,
    COUNT(*) AS record_count
FROM patient_analytics
GROUP BY 1, 2
ORDER BY sort_order;
