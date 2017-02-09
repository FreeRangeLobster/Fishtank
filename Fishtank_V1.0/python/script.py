import webiopi
import datetime
#import MySQLdb
 

#db = MySQLdb.connect("localhost", "monitor", "password", "temps")
#curs=db.cursor() 

GPIO = webiopi.GPIO
from webiopi.devices.serial import Serial
serial = Serial("ttyAMA0", 9600)


#***********************#
#   GPIO Declarations   #
#************************
LIGHT = 17 # GPIO pin using BCM numbering       AUX1
LIGHT2 = 23 # GPIO pin using BCM numbering      WATER PUMP
LIGHT3 = 18 # GPIO pin using BCM numbering      AIR PUMP
LIGHT4 = 22 # GPIO pin using BCM numbering      LIGHT
LIGHT5 = 24 # GPIO pin using BCM numbering      AUX2

#Variable definitions

HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

LIGHT_ON = 17 #Turns ligh on at 5 in the afternoon 
LIGHT_OFF = 19 #Turns ligh on at 9  in the night
  
PUMP_OFF = 18  #Turns pump off 
PUMP_ON  = 19  #Turns pump ON

BUBBLES_ON  = 18  #Turns pump off 
BUBBLES_OFF = 20  #Turns pump ON 

Pressure=0

global TempRead



# setup function is automatically called at WebIOPi startup
def setup():
    global x 
    global y
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

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)


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


#JV 07/02/2017 Commented out from here
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

#try:
#    curs.execute ("""INSERT INTO tempdat 
#            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', 20.6)""")
#    db.commit()

#    print "After Commit"
#    curs.execute ("SELECT * FROM tempdat")
#    print "\nDate       Time        Zone        Temperature"
#    print "==========================================================="

#    for reading in curs.fetchall():
#        print str(reading[0])+" "+str(reading[1])+"     "+reading[2]+"      "+str(reading[3])


#except:
#   print "Error: the database is being rolled back"
#   db.rollback()


#JV 07/02/2017 Commented out to here
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

#def LogTemperature( Temperature, Zone ):
#    sql = "INSERT INTO tempdat(tdate, tTime,zone,Temperature) VALUES (CURRENT_DATE(), NOW(), '%s', '%s' )" % (Zone ,Temperature)
#    curs.execute(sql)
#    db.commit()
#    return True 



# loop function is repeatedly called by WebIOPi 
def loop():
    global x
    global y
    global temperaturevar
    global PressureC
    global TempRead

    
    # retrieve current datetime
#    serial.writeString("S\r")       # write a string
    now = datetime.datetime.now()
            #print(Pressure)

    #Counter up to 30sec
    #- Request Database
    # if there is anything to commit in the database, commit logs, temperature and pressure
    # Update states of the fishtank


    # every second 
    # read arduino


    x = x + 1
    if (x == 10):
        x = 0
        #PressureC = "a"
        
        temperaturevar=measure()
        Zone="Fishtank"
        print(temperaturevar, Zone)
 #       LogTemperature( temperaturevar, Zone )



        #print(temperaturevar)
        #print "Counter =10 seconds time to read configuration Pressure: %s  Temperature: %.2f" % (Pressure, TempRead)

    y = y + 1
    if (y == 5):
        y = 0
  #      print "Counter =10 seconds time to save readings"


    #----------------------------------------------------------------Light------------------------------------------------------
    #for light 4
    # toggle light ON all days at the correct time
    if ((now.hour == LIGHT_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT4) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT4, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == LIGHT_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT4) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT4, GPIO.HIGH)

    #----------------------------------------------------------------Water Pump-----------------------------------------------
    #for light 2
    # toggle light ON all days at the correct time
    if ((now.hour == PUMP_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT2) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT2, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == PUMP_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT2) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT2, GPIO.HIGH)

    
    #------------------------------------------------------------Bubbles Machin3------------------------------------------------
    #for light 3
    # toggle light ON all days at the correct time
    if ((now.hour == BUBBLES_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT3) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT3, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == BUBBLES_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT3) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT3, GPIO.HIGH)

    

    #----------------------------------------------------------------Aux----------------------------------------------------
    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    
    #for light 5
    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT5) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT5, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT5) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT5, GPIO.HIGH)

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
