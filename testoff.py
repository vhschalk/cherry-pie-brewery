import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT) #pump 1
GPIO.setup(27, GPIO.OUT) #heat 1

GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

print("stop test")

#GPIO.cleanup()