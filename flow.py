#!/usr/bin/python
#import os
import time
#import math
#import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up the flow meter
flowing = False
lastPinState = False
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0
litersPoured = 0

#    # Draw LastPinChange
#    text = basicFont.render('Last Pin Change: '+time.strftime('%H:%M:%S', time.localtime(lastPinChange/1000)), True, WHITE, BLACK)
#
#    # Draw PinChange
#    text = basicFont.render('Pin Change: '+time.strftime('%H:%M:%S', time.localtime(pinChange/1000)), True, WHITE, BLACK)
#
#    # Draw PinDelta
#    text = basicFont.render('Pin Delta: '+str(pinDelta) + ' ms', True, WHITE, BLACK)
#
#    # Draw hertz
#    text = basicFont.render('Hertz: '+str(hertz) + 'Hz', True, WHITE, BLACK)
#     
#    # Draw instantaneous speed
#    text = basicFont.render('Flow: '+str(flow) + ' L/sec', True, WHITE, BLACK)
#     
#    # Draw Liters Poured
#    text = basicFont.render('Pints Poured: '+str(pintsPoured) + ' pints', True, WHITE, BLACK)
#    
#    # Draw Pouring
#    text = basicFont.render('Pouring: '+str(flowing), True, WHITE, BLACK)
#     
#    # Draw Pour Start
#    text = basicFont.render('Last Pour Started At: '+time.strftime('%H:%M:%S', time.localtime(pourStart/1000)), True, WHITE, BLACK)
 
# main loop
while True:
    currentTime = int(time.time() * 1000)
    if GPIO.input(22):
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
            litersPoured += flow * (pinDelta / 1000.0000)
    
    print(litersPoured)
    
    lastPinChange = pinChange
    lastPinState = pinDelta

GPIO.cleanup()
