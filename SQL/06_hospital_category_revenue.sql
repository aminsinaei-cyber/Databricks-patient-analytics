-- Break down hospital revenue by service category using a stacked bar chart: hospital, total_revenue, and category as the color grouping.

SELECT hospital, category,
       ROUND(SUM(revenue), 2) AS total_revenue
FROM patient_analytics
GROUP BY hospital, category
ORDER BY hospital, total_revenue DESC;
