import csv
import inspect
import os
from datetime import datetime

current_directory = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

try:
    os.remove(current_directory + '/fixed_data.csv')
except OSError:
    pass

data0 = []
data1 = []

with open('sensor0_log.csv','r') as sensor0, open('sensor1_log.csv','r') as sensor1:
    reader0 = csv.reader(sensor0)
    reader1 = csv.reader(sensor1)
    for row0 in reader0:
        data0.append(row0)
    for row1 in reader1:
        data1.append(row1)
    count = 0
    count1 = 0
    count2 = 0
    for row0 in data0:
        date0 = datetime.strptime(row0[0][:-3],'%m/%d/%Y %H:%M')
        count2 += 1
        for row1 in data1:
            date1 = datetime.strptime(row1[0][:-3],'%m/%d/%Y %H:%M')

            count1 += 1
            if date0 == date1:
                if float(row0[2]) < 100.1 and float(row1[2]) < 100.1:
                    fixed_row = [date0,row0[1],row0[2],row1[1],row1[2]]
                    with open(current_directory+'/fixed_data.csv','a') as file:
                        writer = csv.writer(file)
                        writer.writerow(fixed_row)
                    count = count + 1
                    break
print('Amount of matching dates:' + str(count))
print('count1:' + str(count1))
print('count2:' + str(count2))
