import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

input0 = 'NO_2'
input1 = '2016'
input2 = ''

# Create dataframe with data
data1 = pd.read_csv('madrid_' + input1 + '.csv')

# Convert to datetime format
data1['date'] = pd.to_datetime(data1['date'])

# Create a DatetimeIndex and assign it to the dataframe
data1.index = pd.DatetimeIndex(data1.date)

# Resample the data to a lower frequency, sorted by date, grouped by month
# Note: Apparently the mean() method skips empty rows, results proofed manually by me
columns = ['CO', 'NO_2', 'O_3', 'PM10', 'SO_2']
data1_monthly_mean = data1[columns].resample('M').mean()

# Rename date column with month names (Jan, Feb, etc.)
data1_monthly_mean = data1_monthly_mean.rename(index=lambda x: x.month_name()[:3])

# Select only data from current year (File contains also data from January of the following year)
data1_monthly_mean = data1_monthly_mean.head(n=12)

# Define and initiate parameters needed for plotting the diagram
element = input0
time_period1 = input1
time = data1_monthly_mean.index
values = data1_monthly_mean[element]
unit = ''
if element in ['CO', 'TCH', 'CH4', 'NMHC']:
    unit = 'mg/m³'
else:
    unit = 'μg/m³'

# Plot the diagram based on processed data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(time, values, c='red', label=time_period1,  marker='o')

# If there is a second data file input, repeat the process above
if input2 is not "":
    data2 = pd.read_csv('madrid_' + input2 + '.csv')

    data2['date'] = pd.to_datetime(data2['date'])
    data2.index = pd.DatetimeIndex(data2.date)

    data2_monthly_mean = data2[columns].resample('M').mean()
    data2_monthly_mean = data2_monthly_mean.rename(index=lambda x: x.month_name()[:3])
    data2_monthly_mean = data2_monthly_mean.head(n=12)

    values2 = data2_monthly_mean[element]
    time_period2 = input2
    plt.plot(time, values2, c='blue', label=time_period2, marker='o')
    plt.title("Average " + element + " " + unit + " in Madrid (" + time_period1 + "/" + time_period2 + ")", fontsize=16)
    plt.legend(loc='upper left', fontsize=16)

# Create title using different style if there is only one data series
if input2 is "":
    plt.title("Average " + element + " " + unit + " in Madrid (" + time_period1 + ")", fontsize=16)

plt.grid(True)
plt.ylabel("Average " + element + " " + unit, fontsize=16)
plt.xlabel("Date", fontsize=16)

plt.fill_between(time, values, where=values >= 0,
                facecolor='red', alpha=0.2, interpolate=True)
#plt.fill_between(time, values2, where=values >= 0,
#                facecolor='blue', alpha=0.2, interpolate=True)
plt.show()


barWidth = 0.25
bars1 = values
bars2 = values2
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

plt.bar(r1, bars1, color='red', width=barWidth, edgecolor='white', label=time_period1)
plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='white', label=time_period2)
plt.xticks([r + barWidth/2 for r in range(len(bars1))], time)
plt.ylabel("Average " + element + " " + unit, fontsize=16)
plt.xlabel("Date", fontsize=16)
plt.title("Average " + element + " " + unit + " in Madrid (" + time_period1 + "/" + time_period2 + ")", fontsize=16)
plt.legend(loc='upper left', fontsize=13)
plt.grid(axis='y', b=True)
plt.show()