# Standardization of text values

from pyspark.sql.types import StringType

for field in df_clean.schema.fields:
    if isinstance(field.dataType, StringType):
        df_clean = df_clean.withColumn(
            field.name,
            F.trim(F.col(field.name))
        )
