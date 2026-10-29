# Notebook cell 19
# Original notebook cell 19; run in notebook order.

# Save the final analytics dataset
(
    df_analytics.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("patient.default.patient_analytics")
)

print("Delta table saved successfully!")
