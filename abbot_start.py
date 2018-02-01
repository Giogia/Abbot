#!/usr/bin/env python2

import math
import subprocess
import ThreadHTTPServer
import os
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

    if(roll+pinch>=1 and serverUp == False):
      subprocess.Popen("lxterminal -e sudo python /home/pi/Desktop/Abbot/database_update.py", shell =True)
      subprocess.Popen("sudo python /home/pi/Desktop/Abbot/ThreadHTTPServer.py", shell = True)
      serverUp = True
      neopixel.colorWipe(0,0,255,0)
      
        
    if(roll+pinch<=1 and serverUp == True):
      neopixel.colorWipe(255,255,255,0)
      serverUp = False

    #print(roll+pinch)
    sleep(2)
        
except KeyboardInterrupt:
  print "interrupted from terminal with keyboard"
  neopixel.waveColorDown()
  neopixel.colorWipe(0,0,0,0)
  accelerometer.cleanup()
  serverUp = False
