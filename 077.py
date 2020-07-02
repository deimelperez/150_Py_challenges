list = []
for i in range(0,3):
    list.append(input("Enter a person: "))
ch = input("Do you want to keep inviting people? (y/n): ")
while ch != "n":
    list.append(input("Enter a person: "))
    ch = input("Do you want to keep inviting people? (y/n): ")
print("You have invited", len(list),"people\n")
print(list)
ch = input("Enter a person from the list: ")
ch2 = input("Do you still want to invite it? (y/n): ")
if ch2 == "n":
    list.remove(ch)
print(list)

input("Press enter to continue")
