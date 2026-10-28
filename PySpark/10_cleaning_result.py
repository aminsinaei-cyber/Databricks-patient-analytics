# Cleaning Result

display(df_clean.limit(10))

print("Rows:", df_clean.count())
print("Columns:", len(df_clean.columns))

df_clean.printSchema()
