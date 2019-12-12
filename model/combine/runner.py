#!/usr/bin/env python2
import os

year = 2001
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

def combineMonthAvg(i, year):
    oldDir = os.getcwd()
    dir = 'outputs/output_' + elements[i] + "_" + str(year)
    command = 'cp combineMonthAvg.py ' + dir
    os.system(command)
    os.chdir(dir)
    os.system('pwd') 
    command = './combineMonthAvg.py ' + elements[i] + " " + str(year)
    os.system(command)
    command = 'cp ' + elements[i] + "_" + str(year) + ".csv ../../monthlyAvg/"
    os.system(command)
    os.chdir(oldDir)

year = 2001
i = 0

while year < 2018:
    while i < len(elements):
        combineMonthAvg(i, year)
        i = i + 1
    year = year + 1
    i = 0;

i = 2001
j = i + 1

for e in elements:
    while i < 2018:
        while j < 2018:
            units = "ug/m3"
            if e == "CO":
                units = "mg/m3"
            command = './diagram.py ' + e + " " + str(i) + " " + str(j) + " " + units
            print(command)
            os.system(command)
            j = j + 1
        i = i + 1
        j = i + 1
    i = 2001
    j = i + 1
