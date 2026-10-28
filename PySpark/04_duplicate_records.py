# Duplicate Records

total_rows = df.count()
distinct_rows = df.distinct().count()

print("Total rows:", total_rows)
print("Distinct rows:", distinct_rows)
print("Duplicate rows:", total_rows - distinct_rows)
