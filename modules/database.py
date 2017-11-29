import sqlite3

conn = sqlite3.connect('./Abbot.db', check_same_thread=False)

querycursor = conn.cursor()

# Create basic tables
def create_table():
    querycursor.execute('''CREATE TABLE photos
                 (photo TEXT, label TEXT)''')
    
    querycursor.execute('''CREATE TABLE images
                 (photo TEXT, image TEXT)''')
    
    querycursor.execute('''CREATE TABLE labels
                 (label TEXT PRIMARY KEY, found BOOLEAN)''')
    

# Insert a new label
def insert_label(label, found= False):
    querycursor.execute('''INSERT INTO labels (label,found)
            VALUES (?,?)''',(label,found))
    
# Insert a new image
def insert_image(photo,image):
    querycursor.execute('''INSERT INTO images (photo, image)
            VALUES (?,?)''',(photo,image))

# Insert a new photo
def insert_photo(photo,label= None):
    querycursor.execute('''INSERT INTO photos (photo,label)
            VALUES (?,?)''',(photo,label))
    
# Update a photo label
def update_photo(photo,label):
    querycursor.execute('''UPDATE photos
            SET label = ?
            WHERE photo = ?''',(label,photo))
    
# Update a label              
def update_label(label):
    querycursor.execute('''UPDATE labels
            SET found = ?
            WHERE label = ?''',(True,label))
                        
# Return true if a label exist         
def check_label(label):
    querycursor.execute('''SELECT *
            FROM labels
            WHERE label=?''',(label,))
    return querycursor.fetchone() != None

# Return true if a photo has a certain label
def check_photo_label(photo,label):
    querycursor.execute('''SELECT *
            FROM photos
            WHERE photo = ? AND label = ?''',(photo,label))
    return querycursor.fetchone() != None

# Return true if a photo has a certain images
def check_image(photo,image):
    querycursor.execute('''SELECT *
            FROM images
            WHERE photo = ? AND image = ?''',(photo,image))
    return querycursor.fetchone() != None

def get_photos():
    querycursor.execute('''SELECT photo
            FROM photos''')
    photos = querycursor.fetchall()
    i = 0
    list = []
    for photo in photos:
        list.append(" ".join(map(str, photo)))
    return list
   
    

def get_labels():
    querycursor.execute('''SELECT label
            FROM labels''')
    labels = querycursor.fetchall()
    i = 0
    list = []
    for label in labels:
        list.append(" ".join(map(str, label)))
    return list
   

def get_images():
    querycursor.execute('''SELECT image
            FROM images''')
    images = querycursor.fetchall()
    i = 0
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
