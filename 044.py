num = int(input("Enter number of people: "))
if num > 10:
    print("Too many people")
else:
    for i in range(0,num):
        name = input("Enter name: ")
        print(name, "has been invited")
input("Press enter to continue")
