print('1- Create new file')
print('2- Display the file')
print('3- Add new item to the file')
ch = int(input('Select 1, 2 or 3: '))
while ch != 1 and ch != 2 and ch != 3:
    ch = int(input('Please, select 1, 2 or 3: '))
if ch == 1:
    file = open('109 Subjects.txt','w')
    subject = input("Enter a subject: ")
    file.write(subject + '\n')
    file.close()
elif ch == 2:
    file = open('109 Subjects.txt','r')
    print(file.read())
    file.close()
else:
    file = open('109 Subjects.txt','a')
    subject = input("Enter a subject: ")
    file.write(subject + '\n')
    file.close()
    file = open('109 Subjects.txt','r')
    print(file.read())
    file.close()

input("\nPress enter to continue")
