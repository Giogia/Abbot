import time
import picamera
import database, average_colour, neopixel

camera = picamera.PiCamera()


def take_photo():
  
  #name of the photo
  name = time.strftime("%y%m%d_%H-%M-%S") + ".jpg"

  #capture photo
  neopixel.colorWipe(255,0,0,40)
  time.sleep(4)
  camera.start_preview()
  camera.capture("resources/"+ name)
  camera.stop_preview()
  print "%s captured" %name
  colour = average_colour.average_image_colour(name)
  print(colour)
  #neopixel.colorWipe(colour[0],colour[1],colour[2],0)
  
  #insert photo in database
  database.insert_photo(name)
  database.conn.commit()
  print "%s inserted in database" %name
  neopixel.colorWipe(0,0,0,255)
  

def set_default_settings():
  
  #default settings
  camera.sharpness = 2 #originally 0
  camera.contrast = 5 #originally 0
  camera.brightness = 55 #originally 50
  camera.saturation = 1
  camera.ISO = 0
  camera.video_stabilization = True #originally false
  camera.exposure_compensation = 0
  camera.exposure_mode = 'antishake'
  camera.meter_mode = 'matrix'
  camera.awb_mode = 'auto'
  camera.image_effect = 'denoise'
  camera.color_effects = None
  camera.rotation = 0
  camera.hflip = True #originally false
  camera.vflip = True #originally false
  camera.crop = (0.0, 0.0, 1.0, 1.0)
  
set_default_settings()
  
