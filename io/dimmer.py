import sys
import time
import RPi.GPIO as GPIO

SPI_CS_PIN = 17
SPI_SDISDO_PIN = 22 # mosi
SPI_CLK_PIN = 23

def sleep(a = 0.1):
    time.sleep(a)

# Enables step by step checking by wiring some LEDs to those 3 terminals
def wait_a_key():
    print "waiting..."
    #raw_input()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPI_CS_PIN, GPIO.OUT)
GPIO.setup(SPI_CLK_PIN, GPIO.OUT)
GPIO.setup(SPI_SDISDO_PIN, GPIO.OUT)

GPIO.output(SPI_CLK_PIN, False)
GPIO.output(SPI_SDISDO_PIN, False)
GPIO.output(SPI_CS_PIN, False)

print "Setup"
GPIO.output(SPI_CS_PIN, True)
GPIO.output(SPI_CLK_PIN, False)
GPIO.output(SPI_CS_PIN, False)
wait_a_key()

def set_value(b):
    b = "0000" "00" "{0:010b}".format(b)

    GPIO.output(SPI_CS_PIN, False)
    for x in b:
        GPIO.output(SPI_SDISDO_PIN, int(x))
        GPIO.output(SPI_CLK_PIN, True)
        #For step by step checking: sleep()
        GPIO.output(SPI_CLK_PIN, False)
        #For step by step checking: sleep()

    wait_a_key()

    GPIO.output(SPI_CS_PIN, True)
    sleep()

try:
    for i in range(0, 100, 10):
        print 'set_value:' + str(i)
        set_value(i)
        sleep()
finally:
    GPIO.cleanup()