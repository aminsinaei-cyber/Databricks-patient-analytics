# Final inspection of the new columns

display(
    df_analytics.select(
        F.count("*").alias("total_rows"),
        F.min("length_of_stay").alias("min_stay"),
        F.max("length_of_stay").alias("max_stay"),
        F.round(F.avg("length_of_stay"), 2).alias("avg_stay"),
        F.sum(
            F.col("profit_margin_pct").isNull().cast("int")
        ).alias("null_profit_margins")
    )
)
