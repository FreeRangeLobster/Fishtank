# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 11 # Broadcom pin 11 (P1 pin 23)
ledPin = 9 # Broadcom pin 23 (P1 pin 21)
butPin = 22 # Broadcom pin 22 (P1 pin 15)

TestPin1=24
TestPin2=25
TestPin3=28
TestPin4=7


dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme


GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(TestPin1, GPIO.OUT)
GPIO.setup(TestPin2, GPIO.OUT)
GPIO.setup(TestPin3, GPIO.OUT)
GPIO.setup(TestPin4, GPIO.OUT)


GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output


pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:

        GPIO.output(TestPin1, GPIO.HIGH)
        GPIO.output(TestPin2, GPIO.HIGH)
        GPIO.output(TestPin3, GPIO.HIGH)
        GPIO.output(TestPin4, GPIO.HIGH)

        if GPIO.input(butPin): # button is released
            pwm.ChangeDutyCycle(dc)
            GPIO.output(ledPin, GPIO.LOW)
        else: # button is pressed:
            pwm.ChangeDutyCycle(100-dc)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO