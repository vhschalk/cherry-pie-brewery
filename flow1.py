#!/usr/bin/python
#import os
import time
#import math
#import sys
import RPi.GPIO as GPIO

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up the flow meter
flowing = False
lastPinState = False
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0
flow2 = 0
litersPoured = 0

print("Start flow sensor")

# main loop
while True:
    currentTime = int(time.time() * 1000)
    if GPIO.input(FLOW_SENSOR):
        pinState = True
    else:
        pinState = False

    # If we have changed pin states low to high...
    if(pinState != lastPinState and pinState == True):
        if(flowing == False):
            pourStart = currentTime
            flowing = True
            # get the current time
            pinChange = currentTime
            pinDelta = pinChange - lastPinChange
        if (pinDelta < 1000):
            # calculate the instantanelitersPouredous speed
            hertz = 1000.0000 / 1
            flow = hertz / (60 * 7.5) # L/s
	    flow2 = flow * (pinDelta / 1000.0000)
    
    print(flow)
    
    lastPinChange = pinChange
    lastPinState = pinDelta

GPIO.cleanup()
