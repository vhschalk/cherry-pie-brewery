import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.setup(24, GPIO.OUT)
#GPIO.output(24, 0)

try:
	print "Press now"
	GPIO.wait_for_edge(23, GPIO.FALLING)
	print "Flow!"
	#GPIO.output(24, GPIO.input(17))

except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()