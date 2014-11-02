import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) #pump1
GPIO.setup(27, GPIO.OUT) #valve1

GPIO.output(17, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)

