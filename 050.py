num = 0
while num < 10 or num > 20:
    num = int(input("Enter number between 10 an 20: "))
    if num < 10:
        print("Number too low")
    elif num > 20:
        print("Number too high")

print("Thanks")
input("Press enter to continue")
