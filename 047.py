cond = "y"
total = 0
while cond == "y":
    num = int(input("Enter number: "))
    total += num
    cond = input("Do you want to add another number? (y/n): ")
print("The total is: ",total)
input("Press enter to continue")
