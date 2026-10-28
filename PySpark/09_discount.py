# Inspect minimum, maximum, average, and zero-value counts for Discount. Observed range: 0 to 0.25; this may represent a discount rate.

display(df_clean.select(
    F.min("discount").alias("min_discount"),
    F.max("discount").alias("max_discount"),
    F.avg("discount").alias("avg_discount"),
    F.sum((F.col("discount") == 0).cast("int")).alias("zero_discounts")
))
