# slimMotion by DazRave

# Imports
import RPi.GPIO as GPIO
import time

# Setup GPIOs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             # print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             time.sleep(0.1)

# Connect to database

# functions
def blinkLight ():
    # trigger light

def setZone():
    # set zone


def scanZones():
    # loop over zones
