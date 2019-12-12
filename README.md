# CLO Veronika Yankova, Gasan Nazer, Jonas Lührs
This is the repository of our CLO project- Air pollution

How to execute the model and all relative scripts:

Requirements:
-Installed spark and python

Local mode:
Our pyspark model can be easily executed running the following command in model/combine directory:
spark-submit monthly_avg_spark_fixed.py {element} {year}

Where:
{element} - is one of the five elements that we are using CO, NO_2, O_3, PM10, SO_2
{year} - is one of the years between 2001 and 2017

E.g: spark-submit monthly_avg_spark_fixed.py CO 2001

The output of this execution is a subfolder “output_{element}_{year}” in the folder outputs.
This folder contains 12 different .csv files with the number of the month and the mean for it.

Cluster Mode:
To execute it on this mode you will need a cluster in AWS. The command is the same as for Local mode for a non parallel execution. For a parallel one the command is:
spark-submit --num-executors x --executor-cores y spark-submit monthly_avg_spark_fixed.py {element} {year}

Where:
x- number of executors(worker nodes)
y- number of threads per executor 
{element} - is one of the five elements that we are using CO, NO_2, O_3, PM10, SO_2
{year} - is one of the years between 2001 and 2017



Go to the folder model/combine. Here you will see our dataset(18 csv files- with name madrid_year.csv), 3 directories- diagrams(here are all generated diagrams), monthlyAvg(a folder with combined solutions for a specific element and year), outputs(with a subfolder of every execution of the model). Also in model/combine you can find 3 python scripts- combineMonthAvg.py(script that combines the output of the model to a single csv file), diagram.py(script that creates a diagram for specific years and element) and runner.py(the purpose of this script is to generate all diagrams for every year for the 5 elements that we are interested in. To do that, it executes the model and all other scripts for every element and year. This execution is taking above 30 minutes.).

Requirements:
-Installed spark and python(the scripts are using python 2)
-sudo pip install plot
-sudo apt-get install python-pip
-sudo pip install numpy
-sudo pip install pandas
Command to generate all diagrams execute in /model/combine:
./runner.py

