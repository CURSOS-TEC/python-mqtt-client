
import publisher
import random
from random import randint
import time 
import os
import datetime
#init the publisher object
connected = False
MQTT_publisher = None
try:
	MQTT_publisher = publisher.Publisher()#init the object	
	connected = MQTT_publisher.isConnected# it is connected?
	if(connected):
		print("MQTT publisher is connected")
	else:
		print("MQTT publisher is not connected")
	MQTT_publisher.start()#start the thread
	
except Exception:
	print(" Error MQTT creating the publisher")

try:
	counter = 0
	while connected:
		time.sleep(2)

		value = raw_input('Enter the message:')

		diction = {
			'data' : value
		}
		MQTT_publisher.publish_data(str(diction))
	
except(KeyboardInterrupt, SystemExit,Exception ) as error:
	if(connected): 
		MQTT_publisher.stopPublishing()
	print(error)
	print("bye")
