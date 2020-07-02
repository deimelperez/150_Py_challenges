import csv

file = list(csv.reader(open('111 Books.csv')))
start = int(input('Enter a start year: '))
end = int(input('Enter a start year: '))

tmp = []
for row in file:
    tmp.append(row)
count = 0
x = 0
for row in tmp:
    if start <= int(tmp[x][2]) <= end:
        print(tmp[x])
        count = count + 1
    x = x + 1
if count == 0:
    print('There are no books in that range...')

input("\nPress enter to continue")
