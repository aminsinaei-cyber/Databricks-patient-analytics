-- Show the percentage of each admission priority within each hospital using a stacked bar chart with priority_pct on the Y-axis. The initial record_count version was not normalized to 100%.

SELECT hospital, priority,
       COUNT(*) AS record_count,
       ROUND(
           100.0 * COUNT(*) /
           SUM(COUNT(*)) OVER (PARTITION BY hospital), 2
       ) AS priority_pct
FROM patient_analytics
GROUP BY hospital, priority
ORDER BY hospital, priority;
