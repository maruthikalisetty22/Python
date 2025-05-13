
#################### Creating Df ##################
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SimpleExample").getOrCreate()

# Sample data
data = [(1, "Maruthi", "IT"), (2, "Sai", "Hr")]
# Define schema with string column names
schema = ["ID", "Name", "Department"]
# Create DataFrame
df = spark.createDataFrame(data=data, schema=schema)
# Print schema
df.printSchema()

##################### Creating DF using Struct type ####################
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define schema
schema = StructType([
   Structfield("ID", Integertype(), True),
   Structfield("Name", Stringtype(), True),
   Structfield("Department", Stringtype(), True)
  ])
# Sample data
data = [(1, "Maruthi", "IT"), (2, "Sai", "Hr")]
# Create DataFrame
df_1 = spark.createDataFrame(data=data, schema=schema)
# Show schema
df_1.printSchema()

#################### Data frame operations ###################

#basics
df.show(10, False)
df.head(n)
df.columns
df.distinct().count()
df.count()

#select and filter
df.select("column1","column2")
df.filter("age > 25").select("column1") or df.filter(col("age") > 25).select("column1")
df.where("age > 25 and "city" = 'Hyd'")
df.dropDuplicates()
df.dropDuplicates(["col1", "col2"])

#Column level
df.withColumn("new_age", col("age") *2)
df.withColumnRenamed("old_name", "new_name")
df.drop("column")
df.select(col("age").alias("new_age")
df.select(expr("salary*0.8 as bonus"))
df.withColumn("age_group", when("age") < 18, "Minor").otherwise("Adult"))         

#Aggregrations
df.groupBy("department").count()
df.groupBy("department").agg(avg("salary"), max("salary"))
df.agg(sum("salary").alias("total_salary")

#Sorting
df.sort("name","age")
df.orderBy("age")
df.orderBy(col("age").desc())

#Joins
df1.join(df2, on="id", how="inner)
df1.join(df2, df1.id = df2.student_id, "left")

#Window functions
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

#Row number window 
Windowspec = Window.partitionBy("department").orderBy("salary")
df.withColumn("rank", row_number().over(Windowspec))

##Handling nulls
df.dropna()
df.fillna("N/a")
df.fillna({"col1":0, "col2":"missing"})

#Reading and Writing Data
df = spark.read.csv("path", header=True, inferSchema=True)
df = spark.read.json("path")
df = spark.read.parquet("path")

#Write
df.write.csv("path")
df.write.json("path")
df.write.parquet("path")

#Data type casting
df.withColumn("age", col("age").cast("int"))
#Explode
df.withColumn("exploded_column", explode(col("column")))
