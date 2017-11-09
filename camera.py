import time
import picamera



def take_picture(name):
  
  camera = picamera.PiCamera()
  
  camera.start_preview()
  camera.capture('%s.jpg' %name)
  camera.stop_preview()
  
  

def set_default_camera():
  
  camera = picamera.PiCamera()
  
  #default settings
  camera.sharpness = 0
  camera.contrast = 0
  camera.brightness = 50
  camera.saturation = 0
  camera.ISO = 0
  camera.video_stabilization = False
  camera.exposure_compensation = 0
  camera.exposure_mode = 'auto'
  camera.meter_mode = 'average'
  camera.awb_mode = 'auto'
  camera.image_effect = 'none'
  camera.color_effects = None
  camera.rotation = 0
  camera.hflip = False
  camera.vflip = False
  camera.crop = (0.0, 0.0, 1.0, 1.0)
  

  
