import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
import os
import csv
import datetime

#crontab.guru
#crontab under root aka "sudo crontab -e"
#min  hour  day  month  weekday   command
#*    *       *      *           *               [command]  //this command is to run every minute

sensor_model = dht.DHT22

#GPIO Pin that the sensor is attached to
sensor_pins = [3,15,27]
num_sensors = 2

isRoot = os.getuid() == 0

def logToCSV(temp, humidity, tag):
	row = [datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'), temp, humidity]
	with open('/home/sensors/sensors_finalproject/sensor' + str(tag) + '_log.csv', 'a') as file:
		writer = csv.writer(file)
		writer.writerow(row)

if isRoot:
	humidity = []
	temp = []

	for i in range(0,num_sensors):
		h,t = dht.read_retry(sensor_model,sensor_pins[i])
		humidity.append(h)
		temp.append(t)
		if humidity[i] is None:
			print('Could not read humidity from sensor ' + i)
			humidity[i] = 99999
		if temp[i] is None:
			temp[i] = 99999
			print('Could not read temperature from sensor ' + i)

		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp[i], humidity[i]))
		logToCSV(temp[i],humidity[i],i)

else:
	print("run script as root")


