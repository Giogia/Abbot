#!/usr/bin/env python2

from time import sleep
from modules import adxl345, neopixel

accelerometer = adxl345.ADXL345(interrupt = True)

print "ready"
neopixel.colorWipe(0,255,0,255)
sleep(0.5)
neopixel.colorWipe(0,0,0,255)

try:
  while True:
    sleep(1)
except KeyboardInterrupt:
  print "interrupted from terminal with keyboard"
  accelerometer.cleanup()
