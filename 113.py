import csv

count = int(input('How many books do you want to add? '))
file = open ('111 Books.csv','a')
for i in range(0,count):
    title = input('Enter title: ')
    author = input('Enter author: ')
    date = input('Enter date: ')
    newRecord = title + ',' + author + ',' + date + '\n'
    file.write(str(newRecord))
file.close()

file = open ('111 Books.csv','r')
author = input('Enter an author: ')
reader = csv.reader(file)
count = 0
for row in reader:
    if author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print('There are no books of that author...')
file.close()

input("\nPress enter to continue")
