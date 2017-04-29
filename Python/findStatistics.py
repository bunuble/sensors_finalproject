#!/usr/bin/env python2
import pylab
import numpy as np
import csv
from datetime import datetime

date = []
temp_inside = []
temp_outside = []
humidity_inside = []
humidity_outside = []
temp_diff = []
humidity_diff = []

with open('../CSV/fixed_data.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        if row[0] is not "":
            date.append(datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S'))
            temp_inside.append(float(row[1]))
            humidity_inside.append(float(row[2]))
            temp_outside.append(float(row[3]))
            humidity_outside.append(float(row[4]))
            temp_diff.append(float(row[1])-float(row[3]))
            humidity_diff.append(float(row[2])-float(row[4]))


print("Mean temp inside: " + str(np.mean(temp_inside)))
print("Std Dev temp inside: " + str(np.std(temp_inside)))
print("Mean temp outside: " + str(np.mean(temp_outside)))
print("Std Dev temp outside: " + str(np.std(temp_outside)))
print("Mean humidity inside: " + str(np.mean(humidity_inside)))
print("Std Dev humidity inside: " + str(np.std(humidity_inside)))
print("Mean humidity outside: " + str(np.mean(humidity_outside)))
print("Std Dev humidity outside: " + str(np.std(humidity_outside)))
