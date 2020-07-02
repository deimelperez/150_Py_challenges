list = [[2,5,8],[8,5,6],[2,5,7],[3,7,2]]
print(list)

row = int(input("Select row: "))
print(list[row])
num = int(input("Add number: "))
list[row].append(num)
print(list[row])

input("\nPress enter to continue")
