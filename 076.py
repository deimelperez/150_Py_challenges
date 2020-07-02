list = []
for i in range(0,3):
    list.append(input("Enter a person: "))
ch = input("Do you want to keep inviting people? (y/n): ")
while ch != "n":
    list.append(input("Enter a person: "))
    ch = input("Do you want to keep inviting people? (y/n): ")
print("You have invited", len(list),"people")

input("Press enter to continue")
