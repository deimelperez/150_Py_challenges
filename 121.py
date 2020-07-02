import os

clear = lambda: os.system('cls')
list = []


def prompt():
    ch = 0
    while ch != 1 and ch != 2 and ch != 3 and ch != 4 and ch != 5:
        clear()
        print('1- Add name')
        print('2- Change name')
        print('3- Delete name')
        print('4- View list')
        print('5- Exit')
        ch = int(input('Select an option: '))
        clear()
    return ch


def add_name(list):
    list.append(input('Enter name: '))
    return list


def change_name(list):
    x = 0
    for i in list:
        print(x, '-', i)
    ch = int(input('Select name: '))
    list[ch] = input('Enter new name: ')
    return list


def delete_name(list):
    x = 0
    for i in list:
        print(x, '-', i)
    ch = int(input('Select name you want to delete: '))
    del list[ch]
    return list


def view_name(list):
    x = 0
    for i in list:
        print(x, '-', i)
    input("\nPress enter to continue")
    return


def main():
    ch = 0
    while ch != 5:
        ch = prompt()
        if ch == 1:
            add_name(list)
        elif ch == 2:
            change_name(list)
        elif ch == 3:
            delete_name(list)
        elif ch == 4:
            view_name(list)
    input("\nPress enter to continue")
    return


main()
