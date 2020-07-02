import csv
import random

try:
    file = open('117 Maths.csv', 'x')
except Exception as e:
    file = open('117 Maths.csv', 'a')
name = input('Enter your name: ')
count = 0
x = []
y = []
ans = []
for i in range(0, 2):
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))
    ans.append(int(input("How much is {0} + {1} = ".format(x[i], y[i]))))
    if ans[i] == (x[i] + y[i]):
        count = count + 1
qst1 = str(x[0]) + '+' + str(y[0]) + '=' + str(ans[0])
qst2 = str(x[1]) + '+' + str(y[1]) + '=' + str(ans[1])
newRecord = name + ',' + qst1 + ',' + qst2 + ',' + str(count) + '\n'

file.write(str(newRecord))
file.close()

input("\nPress enter to continue")
