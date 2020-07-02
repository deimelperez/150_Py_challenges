name = input("Enter up(u) or down(d): ")
if name == "u":
    num = int(input("Enter top number: "))
    for i in range(1,num+1):
        print(i)
elif name == "d":
    num = int(input("Enter a number below 20: "))
    for i in range(20,num-1,-1):
        print(i)
else:
    print("I dont understand")

input("Press enter to continue")
