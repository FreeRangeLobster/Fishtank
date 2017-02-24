# -*- coding: utf-8 -*-

import webiopi
import datetime
import MySQLdb
 

#Initialising Database comms
db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor() 

#Initialising serial port to com with arduino
GPIO = webiopi.GPIO
from webiopi.devices.serial import Serial
serial = Serial("ttyAMA0", 9600)

#baton
QueryBaton= "Air"
global QueryBatonNo
QueryBatonNo = 0


#***********************#
#   GPIO Declarations   #
#************************
LIGHT = 17 # GPIO pin using BCM numbering       AUX1
LIGHT2 = 23 # GPIO pin using BCM numbering      WATER PUMP
LIGHT3 = 18 # GPIO pin using BCM numbering      AIR PUMP
LIGHT4 = 22 # GPIO pin using BCM numbering      LIGHT
LIGHT5 = 24 # GPIO pin using BCM numbering      AUX2

#Variable definitions
#global TempRead



# setup function is automatically called at WebIOPi startup
def setup():
    global x 
    global y
    global TimeNextQuery
    global TimeNextLog
    global SamplingTimeQuery_Sec
    global SamplingTimeLog_Sec
    #baton
    global QueryBaton
    QueryBaton= "Air"
    global QueryBatonNo
    QueryBatonNo = 0

    x = 0
    y = 0



    # set the GPIO used by the light to output
    import os
    os.system("sudo modprobe w1-gpio")
    os.system("sudo modprobe w1-therm")


    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)
    GPIO.setFunction(LIGHT2, GPIO.OUT)
    GPIO.setFunction(LIGHT3, GPIO.OUT)
    GPIO.setFunction(LIGHT4, GPIO.OUT)
    GPIO.setFunction(LIGHT5, GPIO.OUT)


    # empty input buffer before starting processing used for 
    # used for pressure sensor
    while (serial.available() > 0):
        serial.readString()

    # retrieve current datetime
    now = datetime.datetime.now()

    #initialising sampling time
    InitialTimeSample = datetime.datetime.now()
    SamplingTimeQuery_Sec=5
    SamplingTimeLog_Sec=6


    TimeNextQuery = InitialTimeSample + datetime.timedelta(seconds=SamplingTimeQuery_Sec)
    TimeNextLog =InitialTimeSample + datetime.timedelta(seconds=SamplingTimeLog_Sec)
    print "Time query: ", TimeNextQuery, "Time next Log: ",TimeNextLog
    print "Initial time sample : ", InitialTimeSample
    

    

    #global PumpQueryTime = ActualTime + 1min
    print "Time in the future"
    TimeToSample= InitialTimeSample + datetime.timedelta(seconds=10)

    #JV disabled it
    #Log events
    #LogEvent(1,1)

    #TimeToSample= InitialTimeSample + datetime.timedelta(minutes=5)
    print TimeToSample

def QueryDatabase(actuator):
 try:
  TmPastTime = datetime.datetime.now() - datetime.timedelta(hours=1)
  PastTime=TmPastTime.strftime("%H:%M")
  print PastTime 

  TmFutureTime = datetime.datetime.now() + datetime.timedelta(hours=1)
  FutueTime=TmFutureTime.strftime("%H:%M") 
  print FutueTime 


 #query DB table schedule and looks for a period of time and a specific output
  #curs.execute ("SELECT * FROM schedule WHERE output = 'pump'  and time BETWEEN '10:00' AND '14:37'")

  query = ("SELECT * FROM schedule WHERE output = %s and time BETWEEN %s AND %s")
  #query = ("SELECT * FROM schedule WHERE output = 'air' and time BETWEEN %s AND %s")
  print "query: ", query, (actuator,PastTime, FutueTime) 
  curs.execute(query, (actuator,PastTime, FutueTime))
 
  
  print "\nOutput    Status      Enable  Time"
  print "==========================================================="
  for reading in curs.fetchall():
   #Shows the whole table retrieved by the query 
   print str(reading[0])+"   "+str(reading[1])+" "+reading[2]+"  "+str(reading[3])
   if str(reading[1])=='ON' and str(reading[2])=='EN':
    return 1   
   elif str(reading[1])=='OFF' and str(reading[2])=='EN': 
    return 0  
   else:
    return 2
  #In case the query was void, the functions returns 2 
  return 2 
 
 except Exception, e:
  db.close()
  print "Error: the database is being rolled back"
  db.rollback()
  raise e




def measure():
    global TempRead
    tmp0 = webiopi.deviceInstance("tmp0")
    # retrieves current temperature 
    TempRead = tmp0.getCelsius() 
    print("Temperature: %.2f" % TempRead)
    return (TempRead)

def measurePressure():
    global Pressure
    serial.writeString("S\r")       # write a string
    now = datetime.datetime.now()
    webiopi.sleep(0.5)

    if (serial.available() > 0):
        data = serial.readString()     # read available data
        lines = data.split("\r\n")     # split lines
        count = len(lines)             # count lines
        lines = lines[0:count-1]       # remove last item from split which is empty
   

        for pair in lines:
            cv = pair.split("-")       # split channel/value
            channel = int(cv[0])
            Pressure = int(cv[1])
            print(Pressure)
    return (Pressure)



@webiopi.macro
def getSensor(arg0):
    global TempRead
    measure()
    return TempRead

# this macro scales sensor value and returns it as percent string
@webiopi.macro
def getSensor2(channel):
    global Pressure
    measurePressure()
    return Pressure

#JV 17/02/2017 Included it back to test connection with the database
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
try:
    curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'Sys Restart', 00.6)""")
    db.commit()

    print "After Commit"
    curs.execute ("SELECT * FROM tempdat")
    print "\nDate       Time        Zone        Temperature"
    print "==========================================================="

    for reading in curs.fetchall():
        print str(reading[0])+" "+str(reading[1])+"     "+reading[2]+"      "+str(reading[3])


except:
   print "Error: the database is being rolled back"
   db.rollback()
#JV 17/02/2017 Included it back
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


#JV 24/02/2017 Included to queri DB
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
##---------- Executes queries of different outputs acording to baton--------##

#---------- Drives outputs and logs states on the DB
def UpdatesActuators(output,state):
	if state == 0:
		print "Turn OFF"
	elif state == 1:
		print "Turn ON"
	else :
		print "Remains the same"
	
	if state == 1 or state == 0:
 		print "Save states to DB"





def Light():
    print "Query DB For Light.\n"
    a=QueryDatabase('light')
    print a
    UpdatesActuators('lignt',a)


def Pump():
    print "Query DB For Pump\n"
    a=QueryDatabase('Pump')
    print a
    UpdatesActuators('Pump',a)

def Air():
    print "Query DB For Air\n"
    a=QueryDatabase('Air')
    print a
    UpdatesActuators('Pump',a)

def CO2():
    print "Query DB For CO2\n"
    a=QueryDatabase('CO2')
    UpdatesActuators('CO2',a)
    print a

#Options to allow the program to go through the outputs
options = {0 : Light,
           1 : Pump,
           2 : Air,
           3 : CO2,
}
#JV 24/02/2017 Included it back
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑







def LogTemperature( Temperature, Zone ):
    sql = "INSERT INTO tempdat(tdate, tTime,zone,Temperature) VALUES (CURRENT_DATE(), NOW(), '%s', '%s' )" % (Zone ,Temperature)
    curs.execute(sql)
    db.commit()
    return True 


# loop function is repeatedly called by WebIOPi 
def loop():
    global x
    global y
    global temperaturevar

    global PressureC
    global TempRead
    global TimeNextQuery
    global QueryBatonNo
    global TimeNextLog
  

    TimeNow = datetime.datetime.now()
    if TimeNow > TimeNextQuery:
        #GPIO.output(RedLed_LHS, GPIO.LOW)
        TimeNextQuery= TimeNow + datetime.timedelta(seconds=SamplingTimeQuery_Sec)
            
        #JV disabled due to there is no functions to handle it yet            
        #print "Baton no: ", QueryBatonNo
            
        temperaturevar=measure()
        Zone="Fishtank"
        print(temperaturevar, Zone)
        
        LogTemperature( temperaturevar, Zone )
        
        pressurevar=measurePressure()
        Zone="Fishtank"
        print(pressurevar, Zone)
        #print ("Baton no: ", QueryBatonNo)
        
        options[QueryBatonNo]()
        if QueryBatonNo >= 3:
        	QueryBatonNo=0
        else:
        	QueryBatonNo = QueryBatonNo + 1

    
# Asks for status of the ARDUINO
#    serial.writeString("S\r")       # write a string
	    # retrieve current datetime
    now = datetime.datetime.now()
            #print(Pressure)

    #Logging of temp
    if TimeNow > TimeNextLog:	
		TimeNextLog= TimeNow + datetime.timedelta(seconds=SamplingTimeLog_Sec)
		print " Log time NOW"
			
  

  

    x = x + 1
    if (x == 10):
        x = 0
        #PressureC = "a"
        
        #temperaturevar=measure()
        #Zone="Fishtank"
        #print(temperaturevar, Zone)
        #LogTemperature( temperaturevar, Zone )



        #print(temperaturevar)
        #print "Counter =10 seconds time to read configuration Pressure: %s  Temperature: %.2f" % (Pressure, TempRead)

    y = y + 1
    if (y == 5):
        y = 0
  #      print "Counter =10 seconds time to save readings"


  

    #Test the sensor reading
    #measure()

    # gives CPU some time before looping again
    webiopi.sleep(1.5)

  
    #serial.writeString("Ch1ON")





# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.HIGH)
    #Light2
    GPIO.digitalWrite(LIGHT2, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT3, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT4, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT5, GPIO.HIGH)

#Turn arduino lights on/off
#serial.writeString("Ch1ON")





#    webiopi.sleep(1)

#    if (serial.available() > 0):
#        data = serial.readString()     # read available data
#        lines = data.split("\r\n")     # split lines
#        count = len(lines)             # count lines
#        lines = lines[0:count-1]       # remove last item from split which is empty
        #data = serial.readString()        # read available data as string
        #print(data)
        #print(count)

#        for pair in lines:
#            cv = pair.split("-")       # split channel/value
#            channel = int(cv[0])
#            Pressure = int(cv[1])
