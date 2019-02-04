from __future__ import print_function
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("RDD_Intro") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # SAMPLE-1: Make dataset based on range and extract RDD from it

    ds = spark.range(10000000)
    print("Count %i" % ds.count())
    print("Count in rdd %i" % ds.rdd.count())

    spark.stop()
