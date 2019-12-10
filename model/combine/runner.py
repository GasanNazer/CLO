#!/usr/bin/env python2
import os

year = 2010
elements = ["CO", "NO_2", "O_3", "PM10", "SO_2"]
i = 0

while year < 2018:
    while i < len(elements):
        myCmd = 'spark-submit monthly_avg_spark_fixed.py '  + elements[i] + " " + str(year)
        os.system(myCmd)
        print("executed")
        i = i + 1
    year = year + 1
    i = 0;
