from __future__ import print_function

import os

from pyspark.sql import SparkSession

# Print metadata and toDebug String
if __name__ == "__main__":
    os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"

    spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("RDD_Intro") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    sc = spark.sparkContext

    cachedInts = sc.textFile("/home/zaleslaw/data/ints").map(lambda x: int(x)).cache()

    # Step 1: Transform each number to its square
    squares = cachedInts.map(lambda x: x * x)

    # Step 2: Filter even numbers
    even = squares.filter(lambda x: x % 2 == 0)
    print(even.collect())

    # Step 3: print RDD metadata
    even.setName("Even numbers")
    print("Name is " + str(even.name()) + " id is " + str(even.id()))
    print(even.toDebugString())

    spark.stop()
