import Adafruit_DHT as dht
import os
import csv
import time

#crontab.guru
#crontab under root aka "sudo crontab -e"
#min  hour  day  month  weekday   command
#*    *       *      *           *               [command]  //this command is to run every minute

sensor_model = dht.DHT22

#GPIO Pin that the sensor is attached to
sensor_1 = 3
sensor_2 = 15
sensor_3 = 27

isRoot = os.getuid() == 0

def logToCSV(temp, humidity, tag):
    row = [time.time(), tag, temp, humidity]
    with open('sensor_log.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)

if isRoot:
    humidity_1,temp_1 = dht.read(sensor_model,sensor_1)
    humidity_2,temp_2 = dht.read(sensor_model,sensor_2)
    humidity_3,temp_3 = dht.read(sensor_model,sensor_3)

    if humidity_1 is not None and temp_1 is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp_1, humidity_1))
	logToCSV(temp_1,humidity_1,1)
    else:
        print("can't read from Sensor 1")
        humidity_1,temp_1 = 99999
        logToCSV(temp_1,humidity_1,1)

    if humidity_2 is not None and temp_2 is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp_2, humidity_2))
	logToCSV(temp_2,humidity_2,2)
    else:
        print("can't read from Sensor 2")
        humidity_2,temp_2 = 99999
        logToCSV(temp_2,humidity_2,2)

    if humidity_3 is not None and temp_3 is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp_3, humidity_3))
        logToCSV(temp_3,humidity_3,3)
    else:
        print("can't read from Sensor 3")
        humidity_3,temp_3 = 99999
	logToCSV(temp_3,humidity_3,3)

else:
    print("run script as root")
    

