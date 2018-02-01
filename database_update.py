#!/usr/bin/env python2

from modules import internet, google_vision, database, scrape, neopixel
from time import sleep
import itertools
import os
    
#internet.wait_for_internet_connection()
print "connection is up, updating database"


for photo in database.get_photos():

    neopixel.waveColorWipe(0,0,255,0,1)
    existing = False
    
    #find if the photo can be added to database
    if not database.check_photo(photo):
        labels = google_vision.find_labels(photo)
        images = google_vision.detect_web(photo) 
        print "new photo found"
        
        for word in labels:
            if database.check_word(word):
                existing = True
                print "existing word found"
                break
          
        if existing == True:

            add_new_word = True
            
            for label in labels:
                
                if not database.check_word(label):
                    if add_new_word == False:
                        continue
                    database.insert_word(label,True)
                    print "added new word: %s" % label 
                    
                else:
                    database.word_found(label)
                    
                if not database.check_label(photo,label):
                    database.insert_label(photo,label)
                    print "inserted new label"
                    neopixel.colorWipe(51,255,153,0)
                    scrape.download_images([label],['high res'],1)
                    neopixel.colorWipe(0,0,255,0)
                    add_new_word = False

            database.photo_checked(photo)
            database.conn.commit()
            
            """for image in itertools.islice(images,3):
                if not database.check_image(photo,image):
                    database.insert_image(photo,image)
                    print "inserted new image"

            database.conn.commit()"""
            
            
        else:
            database.delete_photo(photo)
            database.conn.commit()
            os.remove("/home/pi/Desktop/Abbot/resources/"+photo)
            print "no existing word found, %s deleted from database" % photo
            
print "database is now up to date"
neopixel.waveColorWipe(255,0,0,0,2)
sleep(2)
neopixel.colorWipe(0,0,255,0)
