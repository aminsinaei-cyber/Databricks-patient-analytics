# Derive length of stay, admission month, and the ratio of reported Profit to Revenue. Set profit margin to null when Revenue is zero.

df_analytics = (
    df_clean
    .withColumn("length_of_stay", F.datediff("discharge_date", "admit_date"))
    .withColumn("admission_month", F.date_format("admit_date", "yyyy-MM"))
    .withColumn("profit_margin_pct", F.when(
        F.col("revenue") != 0,
        F.round(F.col("profit") / F.col("revenue") * 100, 2)
    ))
)
display(df_analytics.select(
    "patient_id", "hospital", "admit_date", "discharge_date",
    "length_of_stay", "admission_month", "revenue", "profit",
    "profit_margin_pct"
).limit(15))
