import pylab
import numpy
import csv
from datetime import datetime
from dateutil.parser import parse

dateTime = []
tempInside = []
tempOutside = []
humidityInside = []
humidityOutside = []

count = 0

with open('sensor0_log.csv', 'r') as sensor0, open('sensor1_log.csv', 'r') as sensor1:
	data0 = csv.reader(sensor0)
	data1 = csv.reader(sensor1)
	for row0 in data0:
		date0 = datetime.strptime(row0[0][:-3],'%m/%d/%Y %H:%M')
		for row1 in data1:
			date1 = datetime.strptime(row1[0][:-3],'%m/%d/%Y %H:%M')
			count += 1
			if date0 == date1:
				fixed_row = [date0,row0[1],row0[2],row1[1],row1[2]]
				dateTime.append(date0)
				tempInside.append(row0[1])
				count = count + 1
				print(date0)

print(count)
pylab.plot(dateTime,tempInside)
pylab.show()
