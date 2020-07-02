import csv

file = list(csv.reader(open('111 Books.csv')))

tmp = []
for row in file:
    tmp.append(row)
count = 0
x = 0
for row in tmp:
    print(x, row)
    x = x + 1
input("\nPress enter to continue")
