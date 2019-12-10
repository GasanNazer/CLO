#!/usr/bin/env python2
import os
import sys

element = sys.argv[1]
year = sys.argv[2]
csv_out = element + "_" + year + '.csv'

csv_dir = os.getcwd()
dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write('\n')

for file in csv_list:
   csv_in = open(file)
   for line in csv_in:
      csv_merge.write(line)
   csv_in.close()
csv_merge.close()

print('Finished CSV file : ' + csv_out)