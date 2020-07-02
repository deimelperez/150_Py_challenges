import random

score = 0
for i in range(0,5):
    rn1 = random.randint(1,5)
    rn2 = random.randint(1,5)
    ans = int(input("How much is {0} + {1} = ".format(rn1,rn2)))
    num = rn1 + rn2
    if num == ans:
        score = score + 1

print("You answered right",score,"questions out of 5")
input("Press enter to continue")
