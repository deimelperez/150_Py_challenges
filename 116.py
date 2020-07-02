import csv

file = list(csv.reader(open('111 Books.csv')))
tmp = []
x = 0
for row in file:
    tmp.append(row)
    print(x, row)
    x = x + 1
row = int(input('Select which row you want to delete: '))
del tmp[row]
row = int(input('Select which row you want to change: '))
col = int(input('Select which column you want to change: '))
data = input('Enter new data: ')
tmp[row][col] = data
file = open('111 Books.csv', 'w')
x = 0
for row in tmp:
    newRec = tmp[x][0] + ',' + tmp[x][1] + ',' + tmp[x][2] + '\n'
    file.write(newRec)
    x = x + 1
file.close()
input("\nPress enter to continue")
