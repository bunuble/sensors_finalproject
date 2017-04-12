import Adafruit_DHT as dht
from time import sleep
import os

sensor_model = dht.DHT22

#GPIO Pin that the sensor is attached to
sensor_1 = 3
sensor_2 = 15
sensor_3 = 27

delay = 2
isRoot = os.getuid() == 0

while isRoot:
    humidity_1,temp_1 = dht.read_retry(sensor_model,sensor_1)
    humidity_2,temp_2 = dht.read_retry(sensor_model,sensor_2)
    humidity_3,temp_3 = dht.read_retry(sensor_model,sensor_3)
    
    if humidity_1 is not None and temp_1 is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else
        print("can't read from Sensor 1")
        continue
        
    if humidity_2 is not None and temp_2 is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else
        print("can't read from Sensor 2")
        continue
        
    if humidity_3 is not None and temp_3 is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else
        print("can't read from Sensor 3")
        continue
    
    #time in seconds
    sleep(delay)
    
if isRoot is False:
    print("run script as root")
    
