# Check for negative Revenue, Price, or Cost values and discharge dates earlier than admission dates. All resulting counts were zero.

display(df.select(
    F.sum((F.col("Revenue") < 0).cast("int")).alias("Negative Revenue"),
    F.sum((F.col("Price") < 0).cast("int")).alias("Negative Price"),
    F.sum((F.col("Cost") < 0).cast("int")).alias("Negative Cost"),
    F.sum((F.col("Discharge Date") < F.col("Admit Date")).cast("int")).alias("Invalid Dates")
))
