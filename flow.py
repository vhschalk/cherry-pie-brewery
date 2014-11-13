import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #PUD_UP

global time1
time1_track = int(time.time())

def flowcount1():
	time1_now = int(time.time()
        flow1 = (time1_now - time1_track) / (60 * 7.5)

        time1_track = time1_now

	print flow1 & ' L/s'

GPIO.add_event_detect(17, GPIO.RISING, callback=countPulse)
