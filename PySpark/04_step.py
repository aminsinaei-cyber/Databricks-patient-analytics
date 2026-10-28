# Inspect distributions of Priority, Payor Segment, Category, and Region. The Not Specified category was retained.

for c in ["Priority", "Payor Segment", "Category", "Region"]:
    print(c)
    display(df.groupBy(F.col(f"`{c}`")).count().orderBy(F.desc("count")))
