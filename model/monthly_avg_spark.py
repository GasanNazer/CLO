from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import month
import string

import sys

import matplotlib.pyplot as plt

conf = SparkConf().setMaster('local').setAppName('Monthly Average')
sc = SparkContext(conf = conf)

element = sys.argv[1]
year1 = sys.argv[2]
year2 = sys.argv[3]
counter = 0
numOfYears = 2

if year2 == "":
    numOfYears = 1

while counter < numOfYears:
    if counter == 0:
        year = year1
    else:
        year = year2

    log_txt = sc.textFile("model/madrid_" + year + ".csv")
    sqlContext = SQLContext(sc)
    header = log_txt.first()

    log_txt = log_txt.filter(lambda line: line != header)
    temp_var = log_txt.map(lambda k: k.split(","))
    log_df = temp_var.toDF(header.split(","))

    log_df2 = log_df.groupBy(month("Date").alias("Month")).agg({element: 'mean'}).orderBy("Month")
    log_df2.write.format("csv").save("model/output" + year + ".csv")

    counter = counter + 1

'''
conf = SparkConf().setMaster('local').setAppName('Monthly Average')
sc = SparkContext(conf = conf)

element = sys.argv[1]

log_txt = sc.textFile("model/madrid_2001.csv")
sqlContext = SQLContext(sc)
header = log_txt.first()

log_txt = log_txt.filter(lambda line: line != header)
temp_var = log_txt.map(lambda k: k.split(","))
log_df = temp_var.toDF(header.split(","))

log_df2 = log_df.groupBy(month("Date").alias("Month")).agg({element: 'mean'}).orderBy("Month")
log_df2.show()
log_df2.write.format("csv").save("model/output.csv")
'''

'''
print(log_df2.collect())

log_df2.show()


time_period = "2001"
#time = log_df2.Month.collect()
#ToDo: Fill in brackets below the name of the average column (i.e. 'avg(CO)')
#values = log_df2[0]
print("-------------")
time = log_df2.select('Month').collect()
values = log_df2.select('avg(CO)').collect()
print("----------")

unit = "unknown"
#time = [12,13,14,15,16]
#values = [1,2,3,4,5]

# Plot the diagram based on processed data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(time, values, c='red', label=time_period,  marker='o')
plt.title("Average " + element + " " + unit + " in Madrid (" + time_period + ")", fontsize=16)
plt.grid(True)
plt.ylabel("Average " + element + " " + unit, fontsize=16)
plt.xlabel("Year", fontsize=16)
plt.savefig("model/output.png")
'''