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

#ultrasonic sensor setup
GPIO.setwarnings(False)			#suppresses GPIO warning
GPIO.setmode(GPIO.BOARD)		#set GPIO pin numbering
TRIG = 23				#associate pin 23 to TRIG
ECHO = 24				#associate pin 24 to ECHO
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#temp_1,humidity_1,temp_2,humidity_2,temp_3,humidity_3

isRoot = os.getuid() == 0

def logToCSV(temp, humidity, tag):
	row = [datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'), temp, humidity]
	with open('/home/sensors/sensors_finalproject/sensor' + str(tag) + '_log.csv', 'a') as file:
		writer = csv.writer(file)
		writer.writerow(row)

def readUltraSonic():
        counter = 1
        data=[]

        while (counter<11):
                GPIO.output(TRIG, False)
                time.sleep(.5)
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration*17150
                distance = round(distance,2)
                data.append(distance) #adds to the list
                counter+=1

        data.sort() #sorts the list
        data = data[1:-1] #gets rid of the biggest and smallest number so it won't count any extremes
        average = sum(data)/float(len(data)) #finds the average
        average = round(average,2)

        print(average)
        return average;

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


