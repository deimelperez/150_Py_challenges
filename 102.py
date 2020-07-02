data_set = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    data_set[name] = {"age":age,"shoe size":shoe}
print(data_set)

name = input("Enter a name from the list: ")
print(data_set[name])

input("\nPress enter to continue")
