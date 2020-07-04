import sqlite3


with sqlite3.connect('141_books.db') as db:
    cursor = db.cursor()

date = input('Enter year: ')

cursor.execute("""SELECT books.title,books.date,books.author FROM books WHERE books.date>? ORDER BY books.date """, [date])
for row in cursor.fetchall():
    print(row)
db.close()
input('Press enter to continue...')