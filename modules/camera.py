import time
import picamera
import database, average_colour, neopixel


camera = picamera.PiCamera()


def take_photo():
  
  #name of the photo
  name = time.strftime("%y%m%d_%H-%M-%S") + ".jpg"

  #capture photo
  camera.start_preview()
  time.sleep(2)
  camera.capture("resources/"+ name)
  camera.stop_preview()
  print "%s captured" %name
  neopixel.waveColor(0,0,0,255,3)

  #insert photo in database
  database.insert_photo(name)
  database.conn.commit()
  print "%s inserted in database" %name
  colour = average_image_colour(name)
  neopixel.waveColorWipe(colour,3)
  

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
  
set_default_settings()
  
