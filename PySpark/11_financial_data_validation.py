# Financial Data Validation

financial_cols = ["price", "cost", "revenue", "discount", "profit"]

display(
    df_clean.select(financial_cols).describe()
)
