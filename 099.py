list = [[2,5,8],[8,5,6],[2,5,7],[3,7,2]]
print(list)

row = int(input("Enter row: "))
print(list[row])
col = int(input("Enter column: "))
print(list[row][col])
ch = input("Do you want to change the value? (y/n): ")
if ch == "y":
    num = int(input("Add number: "))
    list[row][col] = num
print(list[row])

input("\nPress enter to continue")
