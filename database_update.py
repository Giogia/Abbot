#!/usr/bin/env python2

from modules import internet, google_vision, database
from time import sleep
import itertools


internet.wait_for_internet_connection()

for photo in database.get_photos():
    
    labels = google_vision.find_labels(photo)
    images = google_vision.detect_web(photo)
    existing = False

    for label in labels:
      if database.check_label(label):
            database.update_photo(photo,label)
            existing = True
            break

database.conn.commit()
    
    if existing == True:
        for label in itertools.islice(labels, 2):
            
            if not database.check_label(label):
                database.insert_label(label)
                
            if not database.check_photo_label(photo,label):
                database.insert_photo(photo,label)
                
        database.update_label(label)
  
            
        for image in images:
            if not database.check_image(photo,image):
                
                database.insert_image(photo,image)
        database.conn.commit()
    else:
        database.delete_photo(photo)
        database.conn.commit()
        
print("database_update.py executed -- database is now up to date")


