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
        if row[0][8:10] == "20":
            date.append(datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S'))
            temp_inside.append(row[1])
            humidity_inside.append(row[2])
            temp_outside.append(row[3])
            humidity_outside.append(row[4])
            temp_diff.append(float(row[1])-float(row[3]))
            humidity_diff.append(float(row[2])-float(row[4]))

f, (graph_1,graph_2,graph_3,graph_4) = pylab.subplots(4,sharex=True)
graph_1.plot(date,temp_inside,label="Inside Temperature (C)")
graph_1.plot(date,temp_outside,label="Outside Temperature (C)")


#pylab.title('Temperature Inside vs Outside')
#pylab.xlabel('Date')
#pylab.ylabel('Temperature (C)')
graph_1.legend()

graph_2.plot(date,humidity_inside,label="Inside Humidity (%)")
graph_2.plot(date,humidity_outside,label="Outside Humidity (%)")
#pylab.title('Humidity Inside vs Outside')
#pylab.xlabel('Date')
#pylab.ylabel('Humidity (Percent)')
graph_2.legend()

graph_3.plot(date,temp_diff,label="Temperature Difference (C)")
#pylab.title('Temperature Difference Inside vs Outside')
#pylab.xlabel('Date')
#pylab.ylabel('Temperature (C)')
graph_3.legend()

graph_4.plot(date,humidity_diff,label="Humidity Difference (%)")
graph_4.legend()

f.subplots_adjust(hspace=0)

pylab.show()


#pylab.title('Temperature and Humidity Differences for 24 hours')
