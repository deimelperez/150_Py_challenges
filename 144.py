import sqlite3

with sqlite3.connect('141_books.db') as db:
    cursor = db.cursor()

name = input('Enter name: ')

cursor.execute("""SELECT * FROM books WHERE author=? ORDER BY books.date """, [name])
file = open('144_books_auth.txt', 'w')
for row in cursor.fetchall():
    file.write(row[1] + ' - ' + row[2] + ' - ' + str(row[3]) + '\n')
db.close()
file.close()
input('Press enter to continue...')
