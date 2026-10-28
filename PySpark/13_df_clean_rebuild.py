# df_clean rebuild

import re
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

# Load the original table
df = spark.table("patient.default.patient_info_raw")

# Standardize column names
df_clean = df

for old_name in df_clean.columns:
    new_name = re.sub(r"\s+", "_", old_name.strip().lower())
    df_clean = df_clean.withColumnRenamed(old_name, new_name)

# Convert ZIP code to string
df_clean = df_clean.withColumn(
    "zip_code",
    F.lpad(F.col("zip_code").cast("string"), 5, "0")
)

# Trim text values
for field in df_clean.schema.fields:
    if isinstance(field.dataType, StringType):
        df_clean = df_clean.withColumn(
            field.name,
            F.trim(F.col(field.name))
        )

print("Rows:", df_clean.count())
print("Columns:", len(df_clean.columns))
