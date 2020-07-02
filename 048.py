cond = "y"
total = 0
while cond == "y":
    name = input("Enter name: ")
    total += 1
    print(name, "has been invited")
    cond = input("Do you want to add another guest? (y/n): ")
print("The total of guests is: ",total)
input("Press enter to continue")
