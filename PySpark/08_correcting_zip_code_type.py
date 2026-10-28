# Correcting Zip Code Type

df_clean = df_clean.withColumn(
    "zip_code",
    F.lpad(F.col("zip_code").cast("string"), 5, "0")
)
