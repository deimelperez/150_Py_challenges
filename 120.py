import random


def addition():
    x = random.randint(5, 25)
    y = random.randint(5, 25)
    ans = []
    ans.append(x + y)
    ans.append(int(input("How much is {0} + {1} = ".format(x, y))))
    print('Correct Answer: ', ans[0])
    print('Your Answer: ', ans[1])
    return ans


def subtraction():
    x = random.randint(25, 50)
    y = random.randint(0, 25)
    ans = []
    ans.append(x - y)
    ans.append(int(input("How much is {0} - {1} = ".format(x, y))))
    print('Correct Answer: ', ans[0])
    print('Your Answer: ', ans[1])
    return ans


def check(ans):
    if ans[0] == ans[1]:
        print('Correct!')
    else:
        print('Incorrect')
        print('The correct answer was: ', ans[0])
    return


print('1- Addition')
print('2- Subtraction')
ch = int(input('Select 1 or 2: '))
while ch != 1 and ch != 2:
    ch = int(input('Please, select 1 or 2: '))
if ch == 1:
    ans_1 = addition()
else:
    ans_1 = subtraction()
check(ans_1)

input("\nPress enter to continue")
