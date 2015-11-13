import webiopi
import datetime

GPIO = webiopi.GPIO

#***********************#
#   GPIO Declarations   #
#************************
LIGHT = 17 # GPIO pin using BCM numbering       AUX1
LIGHT2 = 23 # GPIO pin using BCM numbering      WATER PUMP
LIGHT3 = 18 # GPIO pin using BCM numbering      AIR PUMP
LIGHT4 = 22 # GPIO pin using BCM numbering      LIGHT
LIGHT5 = 24 # GPIO pin using BCM numbering      AUX2



HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

LIGHT_ON = 17 #Turns ligh on at 5 in the afternoon 
LIGHT_OFF = 19 #Turns ligh on at 9  in the night
  
PUMP_OFF = 18  #Turns pump off 
PUMP_ON  = 19  #Turns pump ON

BUBBLES_ON  = 18  #Turns pump off 
BUBBLES_OFF = 20  #Turns pump ON 





# setup function is automatically called at WebIOPi startup
def setup():

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

@webiopi.macro
def getSensor(arg0):
    global TempRead
    measure()
    return TempRead


# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

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
    webiopi.sleep(1)







# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.HIGH)
    #Light2
    GPIO.digitalWrite(LIGHT2, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT3, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT4, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT5, GPIO.HIGH)

