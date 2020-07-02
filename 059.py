import random

rn = random.choice(["b","y","r","g","w"])
num = input("Enter a colour from the list [blue, yellow, red, green, white] (b/y/r/g/w)")
while num != rn:
    if rn == "b":
        num = input("You are probably feeling BLUE right now: ")
    if rn == "y":
        num = input("You are panic YELLOW: ")
    if rn == "r":
        num = input("You are probably RED of stress: ")
    if rn == "g":
        num = input("I bet you are GREEN with envy: ")
    if rn == "w":
        num = input("You are probably feeling WHITE right now: ")

print("You win!",rn,"==",num)
input("Press enter to continue")
