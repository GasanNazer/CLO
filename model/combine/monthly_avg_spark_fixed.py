from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import month
import string

import sys

conf = SparkConf().setMaster('local[8]').setAppName('Monthly Average')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)	

element = sys.argv[1]
year = sys.argv[2]

log_txt = sc.textFile("./madrid_" + year + ".csv")
header = log_txt.first()

log_txt = log_txt.filter(lambda line: line != header)

temp_var = log_txt.map(lambda k: k.split(","))
log_df = temp_var.toDF(header.split(","))


log_df2 = log_df.groupBy(month("Date").alias("Month")).agg({element: 'mean'}).orderBy("Month")
log_df2.write.format("csv").save("outputs/output" + "_" + element + "_" + year)

print(log_df2.collect())
log_df2.show()