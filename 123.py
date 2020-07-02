import os
import csv

clear = lambda: os.system('cls')


def prompt():
    ch = 0
    while ch != 1 and ch != 2 and ch != 3 and ch != 4:
        clear()
        print('1- Add to file')
        print('2- View all records')
        print('3- Delete record')
        print('4- Exit')
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


def delete_record():
    file = list(csv.reader(open('122 Salaries.csv')))
    tem = []
    x = 0
    for row in file:
        tem.append(row)
        print(x, row)
        x = x + 1
    row = int(input('Select which row you want to delete: '))
    del tem[row]
    file = open('122 Salaries.csv', 'w')
    x = 0
    for row in tem:
        newRec = tem[x][0] + ',' + tem[x][1] + '\n'
        file.write(str(newRec))
        x = x + 1
    file.close()
    return


def main():
    ch = 0
    while ch != 4:
        ch = prompt()
        if ch == 1:
            add_to_file()
        elif ch == 2:
            view_records()
        elif ch == 3:
            delete_record()
    input("\nPress enter to continue")
    return


main()
