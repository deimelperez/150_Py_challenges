name = input("Enter name: ")
num = int(input("Enter number of times: "))
if num > 10:
    num = 3
    name = "Too high"
for i in range(0,num):
    print(name)
input("Press enter to continue")
