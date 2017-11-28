from adxl345 import ADXL345
from time import sleep
  
adxl345 = ADXL345(interrupt = True)

try:
  while True:
    sleep(10)
except KeyboardInterrupt:
  print("ciao")
  adxl345.cleanup()
