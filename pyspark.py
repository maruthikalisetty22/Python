
##  

df = df.withColumn("names", split(col("names"), "/")
df = df.select(explode("names").alias("explodes_names"), df.country)


## Split the names, country and get sum of the 50s and 100s

playerdf = df.withColumn("playername", split(df["player"], "-").getitem(0) \
             .withColumn("country", split(df['player'], "-").getitem(1)
            
finaldf = playerdf.withColumn("sum", col("50s") + col("100s")).filter(col(sum) > 50)
