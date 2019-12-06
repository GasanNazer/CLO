import pandas as pd

year = 2001

while 2001 < 2018:
    file_name = 'madrid_' + str(year) + '.csv'
    data = pd.read_csv(file_name)
    data = data[data.date.str.contains(str(year))]
    data.to_csv(file_name, index=False, encoding='utf8')
    year = year + 1
