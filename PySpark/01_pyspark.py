# Read the source table, display sample records, count rows and columns, and inspect the schema.

df = spark.table("patient_info_raw")
display(df.limit(10))
print("Total rows:", df.count())
print("Total columns:", len(df.columns))
df.printSchema()
