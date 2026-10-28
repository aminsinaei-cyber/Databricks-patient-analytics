-- Calculate Pearson correlation coefficients for linear relationships. The project results were approximately 0.0114 and 0.0113, indicating negligible linear correlation.

SELECT
    ROUND(CORR(length_of_stay, revenue), 4) AS stay_revenue_correlation,
    ROUND(CORR(length_of_stay, profit), 4) AS stay_profit_correlation
FROM patient_analytics;
