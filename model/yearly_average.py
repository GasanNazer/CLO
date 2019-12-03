
import pandas as pd
import matplotlib.pyplot as plt

input0 = 'SO_2'
index = 1
yearly_average = []

# Loop ignores 2018 because we only have data for for month
while index < 18:
    year = 2000 + index
    data = pd.read_csv('madrid_' + str(year) + '.csv')
    data['date'] = pd.to_datetime(data['date'])
    data.index = pd.DatetimeIndex(data.date)

    # ToDo: In file 2011 there is no 'NOx' column! For testing I skipped this element
    columns = ['CO', 'NO_2', 'O_3', 'PM10', 'SO_2']
    data_yearly_avg = data[columns].resample('Y').mean()

    data_yearly_avg = data_yearly_avg.rename(index=lambda x: x.year)
    data_yearly_avg = data_yearly_avg.head(n=1)

    avg = data_yearly_avg.iloc[0][input0]

    yearly_average.append([year, avg])
    index = index + 1

# Create the pandas DataFrame
df = pd.DataFrame(yearly_average, columns=['Year', 'Average'])

# Define and initiate parameters needed for plotting the diagram
element = input0
time_period = "2001-2017"
time = df.Year
values = df.Average
unit = ''
if element in ['CO', 'TCH', 'CH4', 'NMHC']:
    unit = 'mg/m³'
else:
    unit = 'μg/m³'

# Plot the diagram based on processed data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(time, values, c='red', label=time_period,  marker='o')
plt.title("Average " + element + " " + unit + " in Madrid (" + time_period + ")", fontsize=16)
plt.grid(True)
plt.ylabel("Average " + element + " " + unit, fontsize=16)
plt.xlabel("Year", fontsize=16)
plt.show()
