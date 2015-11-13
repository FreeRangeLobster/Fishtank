#!/usr/bin/python
# Imports
import webiopi
import time

GPIO = webiopi.GPIO


 #setup function is automatically called at WebIOPi startup
def setup():

    # set the GPIO used by the light to output
    import os
    os.system("sudo modprobe w1-gpio")
    os.system("sudo modprobe w1-therm")


def measure():
    global TempRead
    tmp0 = webiopi.deviceInstance("tmp0")
    # retrieves current temperature 
    TempRead = tmp0.getCelsius() 
    print("Temperature: %f" % TempRead)
    return (TempRead)

def loop():
    #print(" watch dog script running",int(value))
    webiopi.sleep(5)
    

@webiopi.macro
def getSensor(arg0):
    global TempRead
    measure()
    #print ("Sensor macro", int(value))
    return TempRead