from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import month

import sys

import matplotlib.pyplot as plt

conf = SparkConf().setMaster('local').setAppName('Monthly Average')
sc = SparkContext(conf = conf)

element = sys.argv[1]

log_txt = sc.textFile("Madrid2001.csv")
sqlContext = SQLContext(sc)
header = log_txt.first()

log_txt = log_txt.filter(lambda line: line != header)

temp_var = log_txt.map(lambda k: k.split(","))
log_df = temp_var.toDF(header.split(","))

log_df2 = log_df.groupBy(month("Date").alias("Month")).agg({element: 'mean'}).orderBy("Month")
# log_df2.write.format("csv").save("/home/ubuntu/output.csv")


time_period = "2001"
time = log_df2["Month"]
#ToDo: Fill in brackets below the name of the average column (i.e. "agg("CO")")
#values = log_df2[]
unit = "unknown"

# Plot the diagram based on processed data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(time, values, c='red', label=time_period,  marker='o')
plt.title("Average " + element + " " + unit + " in Madrid (" + time_period + ")", fontsize=16)
plt.grid(True)
plt.ylabel("Average " + element + " " + unit, fontsize=16)
plt.xlabel("Year", fontsize=16)
plt.savefig("/home/ubuntu/output.png")
