import sqlite3

conn = sqlite3.connect('Abbot.db')

querycursor = conn.cursor()

# Create basic tables
def create_table():
    querycursor.execute('''CREATE TABLE photos
                 (photo TEXT PRIMARY KEY, laebl TEXT)''')
    querycursor.execute('''CREATE TABLE discovered
                 (label TEXT PRIMARY KEY, found BOOLEAN, url TEXT)''')
    

# Insert a new label
def insert_label(label, found= False, url=None):
    querycursor.execute('''INSERT INTO discovered (label,found,url)
            VALUES (?,?,?)''',(label,found,url))

# Insert a new photo
def insert_photo(name,label= None):
    photo ='%s.jpg' %name
    querycursor.execute('''INSERT INTO photos (photo,label)
            VALUES (?,?)''',(photo,label))

    

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()


# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()