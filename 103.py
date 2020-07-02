data_set = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    data_set[name] = {"age":age,"shoe size":shoe}
print(data_set)

for names in data_set:
    print("Name:", names, "age:", data_set[names]["age"])

input("\nPress enter to continue")
