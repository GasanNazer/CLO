import csv
import matplotlib.pyplot as plt

filename = 'madrid_2001_test.csv'

with open(filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    hours, values, values2 = [], [], []
    for row in reader:
        hours.append(row[0])
        value = float(row[1])
        values.append(value)
        value2 = float(row[4])
        values2.append(value2)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(hours, values, c='red', label='CO')
    plt.plot(hours, values2, c='blue', label='O_3')

    plt.title("CO and O_3 per hour in Madrid 1. January 2001", fontsize=16)
    plt.xlabel('Hour', fontsize=16)
    plt.xticks(rotation=90)
    plt.legend(loc='upper left')

    #fig.autofmt_xdate()
    plt.ylabel("CO in mg/m³, O_3 in μg/m³", fontsize=16)
    plt.tick_params(axis='both', which='major')
    plt.show()

    #plt.savefig('CLO_test_graph.png')

a = ['2019', '2018']
ad = [8, 13]
plt.bar(a, ad, color='red', width=.5)
plt.title("Test bar chart", fontsize=22)
plt.ylabel('Pollutents')
plt.ylim(0, 45)
plt.xlabel('Year')
plt.show()

b = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
bd = [7, 5, 6, 4, 4, 8, 9, 5, 4, 6, 8, 10]
cd = [8, 6, 6, 3, 5, 7, 10, 6, 7, 8, 6, 11]
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(b, bd, c='red', label='CO 2016')
plt.plot(b, cd, c='blue', label='CO 2017')

plt.title("Comparison of the average CO in mg/m³ in 2016 and 2017", fontsize=16)
plt.xlabel('Time in month', fontsize=16)
plt.legend(loc='upper left')

# fig.autofmt_xdate()
plt.ylabel("CO in mg/m³", fontsize=16)
plt.tick_params(axis='both', which='major')
plt.show()
