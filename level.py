import time
import RPi.GPIO as GPIO

# GPIO output = the pin that's connected to "Trig" on the sensor
# GPIO input = the pin that's connected to "Echo" on the sensor

trig_out_pin = 9
echo_in_pin = 11

GPIO.setmode(GPIO.BCM)

GPIO.setup(trig_out_pin,GPIO.OUT)
GPIO.setup(echo_in_pin,GPIO.IN)

GPIO.output(trig_out_pin, GPIO.LOW)

time.sleep(0.5)

# sensor manual says a pulse ength of 10Us will trigger the 
# sensor to transmit 8 cycles of ultrasonic burst at 40kHz and 
# wait for the reflected ultrasonic burst to be received

# to get a pulse length of 10Us we need to start the pulse, then
# wait for 10 microseconds, then stop the pulse. This will 
# result in the pulse length being 10Us.

GPIO.output(trig_out_pin, True)

# wait 10 micro seconds (this is 0.00001 seconds) so the pulse
# length is 10Us as the sensor expects

time.sleep(0.00001)
GPIO.output(trig_out_pin, False)

print "Start echo"

while GPIO.input(echo_in_pin) == 0:
	pass	
signaloff = time.time()

while GPIO.input(echo_in_pin) == 1:
	pass	
signalon = time.time()

timepassed = signalon - signaloff

distance = timepassed * 17150

# return the distance of an object in front of the sensor in cm
print round(distance, 2) , "cm"

GPIO.cleanup()
