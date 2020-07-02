import csv

file = list(csv.reader(open('111 Books.csv')))
start = int(input('Enter a start year: '))
end = int(input('Enter a start year: '))

tem = []
for row in file:
    tem.append(row)
count = 0
x = 0
for row in tem:
    if int(tem[x][2]) >= start and int(tem[x][2]) <= end:
        print(tem[x])
        count = count + 1
    x = x + 1
if count == 0:
    print('There are no books in that range...')

input("\nPress enter to continue")
