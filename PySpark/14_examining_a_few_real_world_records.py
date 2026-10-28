# Examining a few real-world records

from pyspark.sql import functions as F

display(
    df_clean.select(
        "price",
        "discount",
        "revenue",
        "cost",
        "profit"
    ).limit(20)
)
