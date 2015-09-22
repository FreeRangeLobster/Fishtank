import webiopi
import datetime

GPIO = webiopi.GPIO


LIGHT = 17 # GPIO pin using BCM numbering
PUMP=18 #GPIO pin
AIR=21 #GPIO pin
AUX=22 #GPIO pin

HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)
    GPIO.setFunction(PUMP, GPIO.OUT)
    GPIO.setFunction(AIR, GPIO.OUT)
    GPIO.setFunction(AUX, GPIO.OUT)
    GPIO.setFunction(2, GPIO.OUT)
    import os
    os.system("sudo modprobe w1-gpio")
    os.system("sudo modprobe w1-therm")

    # retrieve current datetime
    now = datetime.datetime.now()
    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)
# loop function is repeatedly called by WebIOPi 

def measure():
    global TempRead
    tmp0 = webiopi.deviceInstance("tmp0")
    # retrieves current temperature 
    TempRead = tmp0.getCelsius() 
    print("Temperature: %f" % TempRead)
    return (TempRead)





def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown


@webiopi.macro
def getSensor(arg0):
    global TempRead
    measure()
    #print ("Sensor macro", int(value))
    return TempRead



def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
    GPIO.digitalWrite(PUMP, GPIO.LOW)
    GPIO.digitalWrite(AIR, GPIO.LOW)
    GPIO.digitalWrite(AUX, GPIO.LOW)   


#Can be erased, used just for prototyping
@webiopi.macro
def getLightHours():
    return "%d;%d" % (HOUR_ON, HOUR_OFF)

@webiopi.macro
def setLightHours(on, off):
    global HOUR_ON, HOUR_OFF
    HOUR_ON = int(on)
    HOUR_OFF = int(off)
    return getLightHours()



#controls the GPIO output of the light using two buttons
@webiopi.macro
def outputControlMacroLight(state):
    if(state == "1"):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)
    elif(state == "0"):
        GPIO.digitalWrite(LIGHT, GPIO.LOW)

#controls the GPIO output of the Pump using two buttons
@webiopi.macro
def outputControlMacroPump(state):
    if(state == "1"):
        GPIO.digitalWrite(PUMP, GPIO.HIGH)
    elif(state == "0"):
        GPIO.digitalWrite(PUMP, GPIO.LOW)

#controls the GPIO output of the Air using two buttons
@webiopi.macro
def outputControlMacroAir(state):
    if(state == "1"):
        GPIO.digitalWrite(AIR, GPIO.HIGH)
    elif(state == "0"):
        GPIO.digitalWrite(AIR, GPIO.LOW)

#controls the GPIO output of the Aux using two buttons
@webiopi.macro
def outputControlMacroAux(state):
    if(state == "1"):
        GPIO.digitalWrite(AUX, GPIO.HIGH)
    elif(state == "0"):
        GPIO.digitalWrite(AUX, GPIO.LOW)

#Indicator macros
@webiopi.macro
def get_LightStatus(arg0):
    p0 = GPIO.digitalRead(LIGHT)
    print ('Light')
    print (p0)
    return "%d" % p0 # returns "0" or "1"

@webiopi.macro
def get_PumpStatus(arg0):
    p1 = GPIO.digitalRead(PUMP)
    print ('Pump')
    print (p1)
    return "%d" % p1 # returns "0" or "1"


@webiopi.macro
def get_AirStatus(arg0):
    p2 = GPIO.digitalRead(AIR)
    print ('Air')
    print (p2)
    return "%d" % p2 # returns "0" or "1"

@webiopi.macro
def get_AuxStatus(arg0):
    p3 = GPIO.digitalRead(AUX)
    print ('Aux')
    print (p3)
    return "%d" % p3 # returns "0" or "1"



