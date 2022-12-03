import pyspark
from pyspark.sql import SparkSession
spark= SparkSession.builder.master("local1").appName ("AddNumbers").getOrCreate()
data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rdd= spark.sparkContext.parallelize(data).reduce(lambda a,b:a+b)
print("--------------------")
print(data)
print("--------------------")


