# Standardizing column names

import re
from pyspark.sql import functions as F

df_clean = df

for old_name in df_clean.columns:
    new_name = re.sub(r"\s+", "_", old_name.strip().lower())
    df_clean = df_clean.withColumnRenamed(old_name, new_name)

df_clean.printSchema()
