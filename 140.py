import sqlite3
import os

clear = lambda: os.system('cls')
with sqlite3.connect('139_contacts.db') as db:
    cursor = db.cursor()


def prompt():
    ch = 0
    while ch != 1 and ch != 2 and ch != 3 and ch != 4 and ch != 5:
        clear()
        print('1- View phone book')
        print('2- Add to phone book')
        print('3- Search for surname')
        print('4- Delete person from phone book')
        print('5- Exit')
        ch = int(input('Select an option: '))
        clear()
    return ch


def view_book():
    cursor.execute("SELECT * FROM phones")
    for x in cursor.fetchall():
        print(x)
    return


def add_contact():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone = int(input('Enter phone number: '))
    new_id = int(input('Enter id: '))
    cursor.execute("""INSERT INTO phones(id,first_name,last_name,phone)
    VALUES(?,?,?,?)""", (new_id, first_name, last_name, phone))
    db.commit()
    return


def search_surname():
    last_name = input('Enter last name: ')
    cursor.execute("""SELECT * FROM phones WHERE last_name=?""", [last_name])
    for row in cursor.fetchall():
        print(row)
    return


def delete_name():
    cursor.execute("SELECT * FROM phones")
    for x in cursor.fetchall():
        print(x)
    new_id = int(input('\nEnter id: '))
    cursor.execute("""DELETE FROM phones WHERE id=?""", [new_id])
    return


def main():
    ch = 0
    while ch != 5:
        ch = prompt()
        if ch == 1:
            view_book()
        elif ch == 2:
            add_contact()
        elif ch == 3:
            search_surname()
        elif ch == 4:
            delete_name()
        input("\nPress enter to continue")
    return


main()
db.close()
