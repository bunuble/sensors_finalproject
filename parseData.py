import csv
from datetime import datetime

with open('sensor0_log.csv','r') as sensor0, open('sensor1_log.csv','r') as sensor1:
    data0 = csv.reader(sensor0)
    data1 = csv.reader(sensor1)
    count = 0
    for row0 in data0:
        date0 = datetime.strptime(row0[0][:-3],'%m/%d/%Y %H:%M')

        for row1 in data1:
            date1 = datetime.strptime(row1[0][:-3],'%m/%d/%Y %H:%M')

            if date0 == date1:
                print("match")
                count = count + 1
                break;
print(count)
