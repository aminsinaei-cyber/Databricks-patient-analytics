# Inspect actual sample records to understand possible relationships among Price, Discount, Revenue, Cost, and Profit.

display(df_clean.select("price", "discount", "revenue", "cost", "profit").limit(20))
