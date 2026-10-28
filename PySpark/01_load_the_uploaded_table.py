# Load the uploaded table

df = spark.table("patient.default.patient_info_raw")

# Display sample records
display(df.limit(10))
