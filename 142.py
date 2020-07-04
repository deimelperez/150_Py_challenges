import sqlite3


with sqlite3.connect('141_books.db') as db:
    cursor = db.cursor()


cursor.execute("SELECT * FROM authors")
for x in cursor.fetchall():
    print(x)


place = input('Enter place of birth: ')

cursor.execute("""SELECT books.title,books.date,books.author FROM books,authors WHERE authors.place=? AND 
books.author=authors.name""", [place])
for row in cursor.fetchall():
    print(row)
db.close()
input('Press enter to continue...')