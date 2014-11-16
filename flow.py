import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global time1_track
time1_track = int(time.time())

print("Start flow count") 

def flowcount1(FLOW_SENSOR):
	global time1_track
	time1_now = int(time.time())
	time_diff = time1_now - time1_track
        flow1 = time_diff / (60 * 7.5)

        time1_track = time1_now

	print (time_diff , "l/s")

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=flowcount1)

while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		print '\ncaught keyboard interrupt!, bye'
		GPIO.cleanup()
		sys.exit()


