#!/usr/bin/env python2

import math
import subprocess
import signal
from time import sleep
from modules import adxl345, neopixel

accelerometer = adxl345.ADXL345(interrupt = True)
serverUp = False

print "ready"
neopixel.waveColorWipe(255,0,0,255,0)
sleep(1)
neopixel.waveColorUp(255,255,255,0)

try:
  while True:
    axes = accelerometer.getAxes(True)

    roll = math.fabs(math.atan2(-axes['y'],math.sqrt(axes['x']*axes['x']+axes['z']*axes['z'])))
    pinch = math.fabs(math.atan2(-axes['z'],math.sqrt(axes['x']*axes['x']+axes['y']*axes['y'])))

    if(roll+pinch>=1):
      neopixel.colorWipe(0,0,255,0)
      if(serverUp == False):
        serverUp = True
        process = subprocess.Popen("python database_update.py")
        process = subprocess.Popen("sudo python -m ThreadHTTPServer 8080", shell=True)

    if(roll+pinch<=1 and serverUp == True):
      neopixel.colorWipe(255,255,255,0)

    #print(roll+pinch)
    sleep(2)
        
except KeyboardInterrupt:
  print "interrupted from terminal with keyboard"
  neopixel.waveColorDown()
  neopixel.colorWipe(0,0,0,0)
  accelerometer.cleanup()
  serverUp = False
