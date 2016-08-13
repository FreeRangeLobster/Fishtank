
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