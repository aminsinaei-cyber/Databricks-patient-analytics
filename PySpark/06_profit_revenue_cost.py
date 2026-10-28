# Calculate differences to check whether Profit equals Revenue minus Cost. Most differences were nonzero.

df_validation = df_clean.withColumn(
    "profit_difference",
    F.round(F.col("revenue") - F.col("cost") - F.col("profit"), 2)
)
display(df_validation.groupBy("profit_difference")
        .count().orderBy(F.desc("count")).limit(15))
