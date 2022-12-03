
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()
rdd = spark.sparkContext.textFile("C:/Users/hp/PycharmProjects/pythonProject3/samah.txt")
print(rdd.collect())
wordsRdd = rdd.flatMap(lambda s: s.split(" "))
print(wordsRdd.collect())
pairRDD= wordsRdd.map(lambda s: (s, 1))
pairRDD_Countwords= sorted(pairRDD.reduceByKey(lambda x, y: x+y).collect(), reverse=False)
print(pairRDD_Countwords)
#for i in pairRDD_Countwords:
   # print(i)