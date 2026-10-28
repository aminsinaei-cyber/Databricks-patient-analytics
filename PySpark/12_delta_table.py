# Persist the final dataset for reuse in notebooks and dashboards. Final output: 8,392 rows and 22 columns.

(df_analytics.write.format("delta").mode("overwrite")
 .saveAsTable("patient_analytics"))
print("Delta table saved successfully!")
df_final = spark.table("patient_analytics")
print("Total rows:", df_final.count())
print("Total columns:", len(df_final.columns))
display(df_final.limit(5))
