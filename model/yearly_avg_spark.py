from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import year

import sys

conf = SparkConf().setMaster('local').setAppName('Yearly Average')
sc = SparkContext(conf = conf)

element = sys.argv[1]
yearOfData = 2001

while yearOfData < 2018:
    log_txt = sc.textFile("model/madrid_" + str(yearOfData) + ".csv")
    sqlContext = SQLContext(sc)
    header = log_txt.first()

    log_txt = log_txt.filter(lambda line: line != header)
    temp_var = log_txt.map(lambda k: k.split(","))
    log_df = temp_var.toDF(header.split(","))

    log_df2 = log_df.groupBy(year("Date").alias("Year")).agg({element: 'mean'}).orderBy("Year")
    log_df2.write.format("csv").save("model/output" + str(yearOfData) + ".csv")

    year = year + 1

