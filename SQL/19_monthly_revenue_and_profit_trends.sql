# Monthly revenue and profit trends
# Original notebook cell 21; run in notebook order.

SELECT
    admission_month,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(*) AS record_count
FROM patient.default.patient_analytics
GROUP BY admission_month
ORDER BY admission_month;
