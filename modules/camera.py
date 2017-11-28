import time
import picamera
import database

camera = picamera.PiCamera()

def capture():

  name = time.strftime("%y%m%d_%H-%M-%S") + ".jpg"

  camera.start_preview()
  time.sleep(1)
  camera.capture("../resources"+ name)
  camera.stop_preview()
  
  database.insert_photo(name,None)
  
  

def set_default_settings():
  
  #default settings
  camera.sharpness = 0
  camera.contrast = 0
  camera.brightness = 50
  camera.saturation = 0
  camera.ISO = 0
  camera.video_stabilization = True #originally false
  camera.exposure_compensation = 0
  camera.exposure_mode = 'auto'
  camera.meter_mode = 'average'
  camera.awb_mode = 'auto'
  camera.image_effect = 'none'
  camera.color_effects = None
  camera.rotation = 0
  camera.hflip = True #originally false
  camera.vflip = True #originally false
  camera.crop = (0.0, 0.0, 1.0, 1.0)
  

camera.capture()  
