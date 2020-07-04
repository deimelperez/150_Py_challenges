import sqlite3


with sqlite3.connect('139_contacts.db') as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS phones(
id integer PRIMARY KEY,
first_name text NOT NULL,
last_name text NOT NULL,
phone integer NOT NULL);""")
cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
VALUES("1","Simon","Howels","01223349752")""")
cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
VALUES("2","Karen","Phillips","01223349753")""")
cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
VALUES("3","Darren","Smith","01223349754")""")
cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
VALUES("4","Anne","Jones","01223349755")""")
cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
VALUES("5","Mark","Smith","01223349756")""")
db.commit()
db.close()
