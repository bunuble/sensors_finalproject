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

with open('fixed_data.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        date.append(datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S'))
        temp_inside.append(row[1])
        humidity_inside.append(row[2])
        temp_outside.append(row[3])
        humidity_outside.append(row[4])
        temp_diff.append(float(row[1])-float(row[3]))
        humidity_diff.append(float(row[2])-float(row[4]))

graph_1 = pylab.subplot(1,2,1)
graph_1.plot(date,temp_inside,label="Inside")
graph_1.plot(date,temp_outside,label="Outside")
pylab.title('Temperature Inside vs Outside')
pylab.xlabel('Date')
pylab.ylabel('Temperature (C)')
graph_1.legend()

graph_2 = pylab.subplot(1,2,2)
graph_2.plot(date,humidity_inside,label="Inside")
graph_2.plot(date,humidity_outside,label="Outside")
pylab.title('Humidity Inside vs Outside')
pylab.xlabel('Date')
pylab.ylabel('Humidity (Percent)')
graph_2.legend()

pylab.show()

pylab.plot(date,temp_diff)
pylab.show()
