import random

rn = random.choice(["h","t"])
ch = input("Select Head or Tail (h/t): ")
if ch == rn:
    print("You win!",rn,"==",ch)
else:
    print("Bad luck!",rn,"!=",ch)
input("Press enter to continue")
