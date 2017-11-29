import sqlite3

conn = sqlite3.connect('./Abbot.db', check_same_thread=False)

querycursor = conn.cursor()

# Create basic tables
def create_table():
  
    querycursor.execute('''CREATE TABLE photos
                 (photo TEXT PRIMARY KEY, checked BOOLEAN)''')
    
    querycursor.execute('''CREATE TABLE words
                 (word TEXT PRIMARY KEY, found BOOLEAN)''')
    
    querycursor.execute('''CREATE TABLE labels
                 (photo TEXT, label TEXT)''')
    
     querycursor.execute('''CREATE TABLE images
                 (photo TEXT, image TEXT)''')

        
# Insert a new photo
def insert_label(photo, checked= False):
    querycursor.execute('''INSERT INTO photos (photo,checked)
            VALUES (?,?)''',(photo,checked))
 

# Insert a new word
def insert_label(word, found= False):
    querycursor.execute('''INSERT INTO words (word,found)
            VALUES (?,?)''',(word,found))
 

# Insert a new label
def insert_photo(photo,label):
    querycursor.execute('''INSERT INTO labels (photo,label)
            VALUES (?,?)''',(photo,label))
  

# Insert a new image
def insert_image(photo,image):
    querycursor.execute('''INSERT INTO images (photo, image)
            VALUES (?,?)''',(photo,image))

    
# set if a photo is checked
def photo_checked(photo,checked=True):
    querycursor.execute('''UPDATE photos
            SET checked = ?
            WHERE photo = ?''',(checked,photo))
   

# set if a photo is found              
def word_found(word,found=True):
    querycursor.execute('''UPDATE words
            SET found = ?
            WHERE word = ?''',(found,word))
   

# Return true if a photo is checked
def check_photo(photo):
    querycursor.execute('''SELECT *
            FROM photos
            WHERE photo=? AND checked=?''',(photo,True))
    return querycursor.fetchone() != None
     
    
# Return true if a word exist         
def check_word(word):
    querycursor.execute('''SELECT *
            FROM words
            WHERE word=?''',(label))
    return querycursor.fetchone() != None


# Return true if a photo has a certain label
def check_label(photo,label):
    querycursor.execute('''SELECT *
            FROM labels
            WHERE photo = ? AND label = ?''',(photo,label))
    return querycursor.fetchone() != None


# Return true if a photo has a certain image
def check_image(photo,image):
    querycursor.execute('''SELECT *
            FROM images
            WHERE photo = ? AND image = ?''',(photo,image))
    return querycursor.fetchone() != None


def get_photos():
    querycursor.execute('''SELECT photo
            FROM photos''')
    photos = querycursor.fetchall()
    list = []
    for photo in photos:
        list.append(" ".join(map(str, photo)))
    return list 


def get_words():
    querycursor.execute('''SELECT word
            FROM words''')
    words = querycursor.fetchall()
    list = []
    for word in words:
        list.append(" ".join(map(str, word)))
    return list
   
    
def get_labels(photo)
    querycursor.execute('''SELECT label
            FROM labels
            WHERE photo = ?''',(photo))
    labels = querycursor.fetchall()
    list = []
    for label in labels:
        list.append(" ".join(map(str, label)))
    return list
       
    
def get_images():
    querycursor.execute('''SELECT image
            FROM images''')
    images = querycursor.fetchall()
    list = []
    for image in images:
        list.append(" ".join(map(str, image)))
    return list

  
def delete_photo(photo):
   querycursor.execute('''DELETE FROM photos
            WHERE photo = ?''',(photo,))

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()


# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
