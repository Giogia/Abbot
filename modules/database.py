import sqlite3

conn = sqlite3.connect('Abbot.db')

querycursor = conn.cursor()

# Create basic tables
def create_table():
    querycursor.execute('''CREATE TABLE photos
                 (photo IMAGE PRIMARY KEY, label TEXT)''')
    querycursor.execute('''CREATE TABLE labels
                 (label TEXT PRIMARY KEY, found BOOLEAN, url TEXT)''')
    

# Insert a new label
def insert_label(label, found= False, url=None):
    querycursor.execute('''INSERT INTO discovered (label,found,url)
            VALUES (?,?,?)''',(label,found,url))

# Insert a new photo
def insert_photo(photo,label= None):
    querycursor.execute('''INSERT INTO photos (photo,label)
            VALUES (?,?)''',(photo,label))
    
# Update a photo label
def update_photo(image,word):
    querycursor.execute('''UPDATE photos
            SET label = word
            WHERE photo = image''')
    
# Update a label              
def update_label(word,link):
    querycursor.execute('''UPDATE labels
            SET found = True, url = link
            WHERE label = word''')
            
def check_label(word):
    return querycursor.execute('''SELECT label
            FROM labels
            WHERE label=word''')

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()


# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
