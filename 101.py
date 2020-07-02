data_set = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
"Tom":{"N":3456,"S":2357,"E":8563,"W":1457},
"Anne":{"N":4586,"S":2586,"E":7859,"W":9547},
"Fiona":{"N":7758,"S":7521,"E":1236,"W":5698}}
print(data_set)

row = input("Enter name: ")
col = input("Enter region: ")
print(data_set[row][col])

row = input("Enter the name you want to change: ")
col = input("Enter the region you want to change: ")

data_set[row][col] = int(input("Enter value: "))
print(data_set[row])

input("\nPress enter to continue")
