num = [213,654,890,569]
for i in num:
    print(i)
ch = int(input("Enter a number: "))

if ch in num:
    print(num.index(ch))
else:
    print("The number in not on the list...")

input("Press enter to continue")
