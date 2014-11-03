import os # importing OS module just in-case needed 
import time # Importing Time module
import RPi.GPIO as gpio # Importing RPIO module as gpio


# Initializing GPIO ports
boardRevision = gpio.RPI_REVISION # Clearing previous gpio port settings
gpio.setmode(gpio.BCM) # Use real physical gpio port numbering
gpio.setup(25, gpio.IN, pull_up_down=gpio.PUD_UP) # setting pin 22 as pull up resistor


def glycolFlow():
  glycolCurrentTime = int(time.time())
  glycolErrorStopTime = glycolCurrentTime + 1
  glycolTimingPulse = 0
  while glycolCurrentTime <= glycolErrorStopTime:
       if gpio.input(25) == True:
            if gpio.input(25) == False:
                 glycolTimingPulse += 1
            else:
                 glycolCurrentTime = int(time.time())
       else:
            glycolCurrentTime = int(time.time())

  if glycolTimingPulse != 0:
       glycolStartTime = int(time.time())
       print 'glycol start time', glycolStartTime
       waitTimerglycol = glycolStartTime + 2
       waitTimerCountglycol = int(time.time())
       glycolCount = 0
       print 'glycol count', glycolCount
       while (glycolCount < 15) and (waitTimerCountglycol <= waitTimerglycol) :
            if gpio.input(25) == True:
                 if gpio.input(25) == False:
                      glycolCount += 1
                      print 'glycol count', glycolCount
                      waitTimerglycol = int(time.time()) + 1
                 else:
                      waitTimerCountglycol = int(time.time())
            else:
                 waitTimerCountglycol = int(time.time())
      glycolEndTime = int(time.time())
       print 'glycol end time', glycolEndTime
       if glycolCount == 15:
            glycolSecsPerLiters = glycolEndTime - glycolStartTime
            glycolLitersPerHour = (3600.0 / glycolSecsPerLiters) * 30
            glycolGalPerHour = glycolLitersPerHour * 0.26417205235815
            return glycolGalPerHour
       else:
            glycolGalPerHour = 0
       return glycolGalPerHour
  else:
       glycolGalPerHour = 0
       return glycolGalPerHour

while True:
  glycolGalPerHour = glycolFlow()
  print "glycol flow =", glycolGalPerHour, "Gal/Hour"
