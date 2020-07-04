import os

clear = lambda: os.system('cls')
base = 'abcdefghijklmnopqrstuvwxyz '


def prompt():
    ch = 0
    while ch != 1 and ch != 2 and ch != 3:
        clear()
        print('1- Make a code')
        print('2- Decode message')
        print('3- Exit')
        ch = int(input('\nSelect an option: '))
        clear()
    return ch


def encode():
    cond1 = True
    while cond1:
        msg = input('Enter message: ')
        cond2 = True
        for letter in msg:
            if letter not in base:
                print('The message should only contain abcdefghijklmnopqrstuvwxyz[ ] in lowercase')
                cond2 = False
                break
        if cond2:
            cond1 = False
    num = int(input('Enter shift number: '))
    for letter in msg:
        if letter == ' ':
            enc = 26 + num
        else:
            enc = ord(letter) - 97 + num
        if enc > 26:
            tmp = enc - 27
            ltr = base[tmp]
        else:
            ltr = base[enc]
        print(ltr, end='')
    return


def decode():
    cond1 = True
    while cond1:
        msg = input('Enter message: ')
        cond2 = True
        for letter in msg:
            if letter not in base:
                print('The message should only contain abcdefghijklmnopqrstuvwxyz[ ] in lowercase')
                cond2 = False
                break
        if cond2:
            cond1 = False
    num = int(input('Enter shift number: '))
    for letter in msg:
        if letter == ' ':
            enc = 26 - num
        else:
            enc = ord(letter) - 97 - num
        if enc < 0:
            tmp = enc + 27
            ltr = base[tmp]
        else:
            ltr = base[enc]
        print(ltr, end='')
    return


def main():
    ch = 0
    while ch != 3:
        ch = prompt()
        if ch == 1:
            encode()
        elif ch == 2:
            decode()
        input("\nPress enter to continue")
    return


main()
