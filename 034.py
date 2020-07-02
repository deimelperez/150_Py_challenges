sel = int(input("""Select an option:
1-Square
2-Triangle
"""))
if sel == 1:
    side = int(input("Enter the length of a side:"))
    area = side**2
elif sel == 2:
    height = int(input("Enter the height:"))
    base = int(input("Enter the base:"))
    area = (height * base)/2
else:
    area = "error"

print(area)
