import random

rn = random.randint(1,5)
num = int(input("Guess a number between 1 and 5: "))
while num != rn:
    num = int(input("Guess again: "))
print("You win!",rn,"==",num)
input("Press enter to continue")
