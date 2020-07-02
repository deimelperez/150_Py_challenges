import random

rn = random.randint(1,5)
num = int(input("Guess a number between 1 and 5: "))
count = 0
while num != rn and count < 1:
    count += 1
    if num > rn:
        num = int(input("Too high, guess again: "))
    else:
        num = int(input("Too low, guess again: "))

if num == rn:
    print("You win!",rn,"==",num)
else:
    print("You lose!",rn,"!=",num)


input("Press enter to continue")
