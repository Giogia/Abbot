#!/usr/bin/env python2

from time import sleep
from modules import accelerometer

accelerometer = ADXL345(interrupt = True)

print("ready")
#TODO green led to say it's ready
try:
  while True:
    sleep(1)
except KeyboardInterrupt:
  print("interrupted from terminal with keyboard")
  accelerometer.cleanup()
