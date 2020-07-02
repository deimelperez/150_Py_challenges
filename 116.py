import csv

file = list(csv.reader(open('111 Books.csv')))
tem = []
x = 0
for row in file:
    tem.append(row)
    print(x, row)
    x = x + 1
row = int(input('Select which row you want to delete: '))
del tem[row]
row = int(input('Select which row you want to change: '))
col = int(input('Select which column you want to change: '))
data = input('Enter new data: ')
tem[row][col] = data
file = open('111 Books.csv', 'w')
x = 0
for row in tem:
    newRec = tem[x][0] + ',' + tem[x][1] + ',' + tem[x][2] + '\n'
    file.write(newRec)
    x = x + 1
file.close()
input("\nPress enter to continue")
