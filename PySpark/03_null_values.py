# Null Values

from pyspark.sql import functions as F

null_counts = df.select([
    F.sum(F.col(f"`{c}`").isNull().cast("int")).alias(c)
    for c in df.columns
])

display(null_counts)
