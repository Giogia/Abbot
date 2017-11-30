#!/usr/bin/env python2

from modules import internet, google_vision, database
from time import sleep
import itertools


internet.wait_for_internet_connection()
print "connection is up, updating database"

for photo in database.get_photos():
    
    existing = False
    
    if not database.check_photo(photo):
        labels = google_vision.find_labels(photo)
        images = google_vision.detect_web(photo) 
        print "new photo found"
        
    for word in words:
        if database.check_word(label):
            existing = True
            print "existing word found"
            break
        
    if existing == True:
        for label in itertools.islice(labels, 2):
            
            if not database.check_word(label):
                database.insert_word(label)
                print "added new word: %s" % label
                
            if not database.check_label(photo,label):
                database.insert_label(photo,label)
                print "inserted new label"
                
        database.conn.commit()
        
        for image in images:
            if not database.check_image(photo,image):
                database.insert_image(photo,image)
                print "inserted new image"
                
        database.conn.commit()
        
    else:
        database.delete_photo(photo)
        database.conn.commit()
        print "no existing word found, %s deleted from database" % photo
        
print "database is now up to date"


