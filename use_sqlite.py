import sqlite3

conn = sqlite3.connect('study.db')

print("sqlite opened")

c = conn.cursor()

c.execute('''CREATE TABLE Book
       (ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
       TITLE           TEXT    NOT NULL,
       WORDNUM          INT     NOT NULL);''')

conn.commit()
print("Table Book created successfully")
conn.close()
