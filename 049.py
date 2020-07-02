compnum = 50
num = 0
total = 0
while compnum != num:
    num = int(input("Enter number: "))
    if num < compnum:
        print("Number too low")
    else:
        print("Number too high")
    total += 1
print("Well done, you took ", total,"attempts")
input("Press enter to continue")
