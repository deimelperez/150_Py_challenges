file = open('106 Names.txt','r')
print(file.read())
file.close()
name = input("Enter a name from the list: ") + '\n'
file = open('106 Names.txt','r')
for row in file:
    print(row)
    if row != name:
        file = open('110 Names2.txt','a')
        file.write(row)
        file.close()

input("\nPress enter to continue")
