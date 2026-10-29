# Notebook cell 20
# Original notebook cell 20; run in notebook order.

df_final = spark.table("patient.default.patient_analytics")

print("Total rows:", df_final.count())
print("Total columns:", len(df_final.columns))

display(df_final.limit(5))
