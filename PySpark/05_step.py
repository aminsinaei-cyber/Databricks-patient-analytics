# Convert column names to snake_case, format ZIP codes as five-character strings, and trim leading/trailing whitespace. No records were removed.

import re
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

df_clean = df
for old_name in df_clean.columns:
    new_name = re.sub(r"\s+", "_", old_name.strip().lower())
    df_clean = df_clean.withColumnRenamed(old_name, new_name)

df_clean = df_clean.withColumn(
    "zip_code", F.lpad(F.col("zip_code").cast("string"), 5, "0")
)
for field in df_clean.schema.fields:
    if isinstance(field.dataType, StringType):
        df_clean = df_clean.withColumn(field.name, F.trim(F.col(field.name)))

display(df_clean.limit(10))
print("Rows:", df_clean.count())
print("Columns:", len(df_clean.columns))
df_clean.printSchema()
