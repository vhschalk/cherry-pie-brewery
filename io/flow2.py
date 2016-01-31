#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys

GPIO.cleanup()

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
	global count
	count = count+1
	print count

print "Start flow count"

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)


while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		print '\ncaught keyboard interrupt!, bye'
		GPIO.cleanup()
		sys.exit()