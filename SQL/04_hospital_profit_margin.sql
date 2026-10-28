-- Calculate each hospital’s aggregate reported profit margin as SUM(profit) / SUM(revenue), not the average of row-level margins; display as a horizontal bar chart.

SELECT hospital,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       ROUND(100.0 * SUM(profit) / NULLIF(SUM(revenue), 0), 2) AS profit_margin_pct
FROM patient_analytics
GROUP BY hospital
ORDER BY profit_margin_pct DESC;
