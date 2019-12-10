#!/usr/bin/env python2
import pandas as pd
import matplotlib.pyplot as plt
import sys

element = sys.argv[1]
time_period = sys.argv[2]
time_period2 = sys.argv[3]
unit = sys.argv[4]

dir = "monthlyAvg/"

df_year1 = pd.read_csv(dir + element + "_" + time_period + ".csv", index_col='month', names=['month', 'avg'])
df_year2 = pd.read_csv(dir + element + "_" + time_period2 + ".csv", index_col='month', names=['month', 'avg'])

#sort the dfs
df_year1.sort_index(inplace=True)
df_year2.sort_index(inplace=True)

# Plot the diagram based on processed data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(df_year1.index, df_year1.values, c='red', label=time_period,  marker='o')
plt.plot(df_year2.index, df_year2.values, c='blue', label=time_period2,  marker='o')
plt.title("Average " + element + " " + unit + " in Madrid (" + time_period + "/" + time_period2 + ")", fontsize=16)
plt.grid(True)
plt.ylabel(element + " " + unit, fontsize=16)
plt.xlabel("Month", fontsize=16)
plt.legend(loc='upper left', fontsize=16)
dir_save = "diagrams/"
plt.savefig(dir_save + element + "_" + time_period + "_" + time_period2 + ".png")