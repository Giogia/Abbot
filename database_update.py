#!/usr/bin/env python2


from modules import internet, google_vision, database, scrape
from time import sleep
import itertools
import os


internet.wait_for_internet_connection()
print "connection is up, updating database"

for photo in database.get_photos():
    
    existing = False
    
    if not database.check_photo(photo):
        labels = google_vision.find_labels(photo)
        images = google_vision.detect_web(photo) 
        print "new photo found"
        
    for word in labels:
        if database.check_word(word):
            database.word_found(word)
            existing = True
            print "existing word found"
            scrape.download_images([word],['high res'],1)
            break
        
    database.conn.commit()
        
    if existing == True:

        count = 0
        
        for label in labels:
            
            if not database.check_word(label):
                if count >= 2:
                    continue
                database.insert_word(label,True)
                print "added new word: %s" % label
                
            if not database.check_label(photo,label):
                database.insert_label(photo,label)
                print "inserted new label"
                scrape.download_images([label],['high res'],1)
                
            count +=1

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
        os.remove("./resources/"+photo)
        print "no existing word found, %s deleted from database" % photo
        
print "database is now up to date"


