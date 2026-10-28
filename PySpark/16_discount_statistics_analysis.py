# Discount Statistics Analysis

display(
    df_clean.select(
        F.min("discount").alias("min_discount"),
        F.max("discount").alias("max_discount"),
        F.avg("discount").alias("avg_discount"),
        F.sum((F.col("discount") == 0).cast("int")).alias("zero_discounts")
    )
)
