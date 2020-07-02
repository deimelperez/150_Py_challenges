total = 0
for i in range(0,5):
    num = int(input("Enter number: "))
    n = input("Do you want it included? (y or n): ")
    if n == "y":
        total += num
print(total)
input("Press enter to continue")
