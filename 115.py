import csv

file = list(csv.reader(open('111 Books.csv')))

tem = []
for row in file:
    tem.append(row)
count = 0
x = 0
for row in tem:
    print(x, row)
    x = x + 1
input("\nPress enter to continue")
