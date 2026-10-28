-- Calculate revenue, reported profit, record count, and revenue share by service category; use the same dataset for revenue bars, profit bars, and a revenue donut chart.

SELECT category,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS service_records,
       ROUND(100.0 * SUM(revenue) / SUM(SUM(revenue)) OVER (), 2) AS revenue_share_pct
FROM patient_analytics
GROUP BY category
ORDER BY total_revenue DESC;
