#Title: Communication to FishTank_Arduino_board
#Version             Description                          Date                       Changes
#1A              Testing communication Pi and Arduino    27/08/2016               Initial program
#Date: 27/08/2016
#Developer: Juan Vivas, www.freerangelobster.blogspot.co.uk, 
#Description:
#Sends information to arduino using raspberry pi serial port. Updates 5 PWM channels supdates the digital
#and request information from the pressure sensor
#//Based on: Arduino code samples
#//Note: The Arduino board is 5V based, the Raspberry pi board is 3.3V based. In order to couple the voltage between 
#//the two boards it was required to use a voltage devider between the TX of the arduino and the RX of the Pi. The
#//resistors used where 4k7 and 2k5
#//COMMANDS
#//Queries from Raspberry        Replies from Arduino      Command
#//- Arduino Status       [Ch status, Pres] 11111-999         S
#//- Get Pressure                      P xxxx                 P
#//- Channel1 On                       _Ch1ON                Ch1ON
#//- Channel2 On                       _Ch2ON                Ch2ON
#//- Channel3 On                       _Ch3ON                Ch3ON
#//- Channel4 On                       _Ch4ON                Ch4ON
#//- Channel5 On                       _Ch5ON                Ch5ON
#//- Channel1 Off                      _Ch1OFF               Ch1OFF
#//- Channel2 Off                      _Ch2OFF               Ch2OFF
#//- Channel3 Off                      _Ch3OFF               Ch3OFF
#//- Channel4 Off                      _Ch4OFF               Ch4OFF
#//- Channel5 Off                      _Ch5OFF               Ch5OFF
                 
#//Software serial enabled for debugging proposes
#//*/

#!/usr/bin/python

import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()



try:
    while 1:
		ser.write("Ch1ON")
		response = ser.readline()
		print response
		time.sleep(1)

		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


		ser.write("Ch2ON")
		response = ser.readline()
		print response
		time.sleep(1)

		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


		
		ser.write("Ch3ON")
		response = ser.readline()
		time.sleep(1)
		print response

		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


		ser.write("Ch4ON")
		response = ser.readline()
		print response
		time.sleep(1) 


		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)

		
		ser.write("Ch5ON")
		response = ser.readline()
		print response
		time.sleep(1)


		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


		ser.write("Ch1OFF")
		response = ser.readline()
		print response
		time.sleep(1) 
		

		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


		ser.write("Ch2OFF")
		response = ser.readline()
		print response
		time.sleep(1)
		
		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)



		ser.write("Ch3OFF")
		response = ser.readline()
		time.sleep(1)
		print response
		
		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)



		ser.write("Ch4OFF")
		response = ser.readline()
		print response
		time.sleep(1) 
		
		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)



		ser.write("Ch5OFF")
		response = ser.readline()
		print response
		time.sleep(1) 

		ser.write("S")
		response = ser.readline()
		print response
		time.sleep(1)


        #response = ser.readline()
        #print response

except KeyboardInterrupt:
    ser.close()
