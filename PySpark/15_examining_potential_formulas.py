# Examining potential formulas

financial_check = df_clean.select(
    F.round(
        F.col("revenue") - F.col("cost") - F.col("profit"), 2
    ).alias("diff_profit_basic"),

    F.round(
        F.col("revenue") - F.col("cost") -
        F.col("discount") - F.col("profit"), 2
    ).alias("diff_profit_discount"),

    F.round(
        F.col("price") - F.col("discount") -
        F.col("revenue"), 2
    ).alias("diff_revenue")
)

display(
    financial_check.select(
        *[
            F.sum(
                (F.abs(F.col(c)) < 0.01).cast("int")
            ).alias(c + "_matches")
            for c in financial_check.columns
        ]
    )
)
