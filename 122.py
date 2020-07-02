import os
import csv

clear = lambda: os.system('cls')


def prompt():
    ch = 0
    while ch != 1 and ch != 2 and ch != 3:
        clear()
        print('1- Add to file')
        print('2- View all records')
        print('3- Exit')
        ch = int(input('Select an option: '))
        clear()
    return ch


def add_to_file():
    file = open('122 Salaries.csv', 'a')
    name = input('Enter name: ')
    salary = input('Enter salary: ')
    record = name + ',' + salary + '\n'
    file.write(str(record))
    file.close()
    return


def view_records():
    file = open('122 Salaries.csv', 'r')
    for row in file:
        print(row)
    file.close()
    input("\nPress enter to continue")
    return


def main():
    ch = 0
    while ch != 3:
        ch = prompt()
        if ch == 1:
            add_to_file()
        elif ch == 2:
            view_records()
    input("\nPress enter to continue")
    return


main()
