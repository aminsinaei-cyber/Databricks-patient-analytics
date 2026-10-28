# Count nulls in every column and identify exact duplicate rows. Results: zero nulls and zero exact duplicates; repeated Patient IDs are not necessarily duplicate records.

from pyspark.sql import functions as F
null_counts = df.select([
    F.sum(F.col(f"`{c}`").isNull().cast("int")).alias(c)
    for c in df.columns
])
display(null_counts)
total_rows = df.count()
distinct_rows = df.distinct().count()
print("Total rows:", total_rows)
print("Distinct rows:", distinct_rows)
print("Duplicate rows:", total_rows - distinct_rows)
