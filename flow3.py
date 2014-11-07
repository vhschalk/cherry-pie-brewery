#!/usr/bin/python
#import os
import time
#import math
#import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(17):
	print("flow")
else:
	print("no flow")

GPIO.cleanup()
