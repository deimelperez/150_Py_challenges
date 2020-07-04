import sqlite3


with sqlite3.connect('141_books.db') as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS authors(
name text NOT NULL,
place text NOT NULL);""")
cursor.execute("""INSERT INTO authors(name,place)
VALUES("Agatha Christie","Torquay")""")
cursor.execute("""INSERT INTO authors(name,place)
VALUES("Cecelia Ahern","Dublin")""")
cursor.execute("""INSERT INTO authors(name,place)
VALUES("J.K. Rowling","Bristol")""")
cursor.execute("""INSERT INTO authors(name,place)
VALUES("Oscar Wild","Dublin")""")

cursor.execute("""CREATE TABLE IF NOT EXISTS books(
id integer NOT NULL,
title text NOT NULL,
author text NOT NULL,
date int NOT NULL);""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("1","De Profundis","Oscar Wilde","1905")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("2","Harry Potter and the chamber of secrets","J.K. Rowling","1998")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("3","Harry Potter and the prisoner of Azkaban","J.K. Rowling","1999")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("4","Lyrebird","Cecelia Ahern","2017")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("5","Murder on the Orient Express","Agatha Christie","1905")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("6","Perfect","Cecelia Ahern","2017")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("7","The marble collector","Cecelia Ahern","2016")""")
cursor.execute("""INSERT INTO books(id,title,author,date)
VALUES("8","The murder on the links","Agatha Christie","1923")""")

db.commit()
db.close()
