# Values ​​of the categorical columns

for column in ["Priority", "Payor Segment", "Category", "Region"]:
    print(f"\n--- {column} ---")
    df.groupBy(column).count().orderBy(F.desc("count")).show(30, truncate=False)
