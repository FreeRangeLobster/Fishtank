#!/usr/bin/python

import serial
import time



ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

#ser.write('Ch1OFF')
ser.write('Ch1ON')

try:
    while 1:
    	response = ser.readline()
    	print response
    	
#    	ser.write('P')
#    	time.sleep(1)
#    time.sleep(1)
#	ser.write('off')

	#Testing communication using all commands
	#Pressure]
	#ser.write('Ch1ON')
	#time.sleep(1)
	
	#ser.write('Ch2ON')
	#time.sleep(1)

	#ser.write('Ch3ON')
	#time.sleep(1)

	#ser.write('Ch4ON')
	#time.sleep(1)

	#ser.write('Ch5ON')
	#time.sleep(1)



except KeyboardInterrupt:
    ser.close()