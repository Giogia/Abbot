from modules import *
from time import sleep

While True:
    internet.wait_for_internet_connection()

    for photo in database.get_photos():
        
        labels = google_vision.find_labels(photo)
        images = google_vision.detect_web(photo)
        existing = False

        for label in labels:
          if database.check_label(label):
                database.update_photo(photo,label)
                database.conn.commit()
                existing = True
                break
                
        if existing == True:
            for label in labels:
                
                if not database.check_label(label):
                    database.insert_label(label)
                    
                if not database.check_photo_label(photo,label):
                    database.insert_photo(photo,label)
                    
                database.update_label(label)
                database.conn.commit()
                
            for image in images:
                if not database.check_image(photo,image):
                    
                    database.insert_image(photo,image)
                    database.conn.commit()
        else:
            database.delete_photo(photo)
            database.conn.commit()

    sleep(300)

