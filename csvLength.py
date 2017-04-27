import csv

with open('CSV/fixed_data.csv') as file:
    data = csv.reader(file)
    print(len(list(data)))
