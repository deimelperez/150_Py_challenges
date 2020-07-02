file = open('106 Names.txt','a')
file.write(input('Enter name: ')+'\n')
file.close()
file = open('106 Names.txt','r')
print(file.read())
file.close()

input("\nPress enter to continue")
