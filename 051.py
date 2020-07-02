num = 1
num = int(input("Enter a number: "))
ans = 0
while num > 0:
    print("There are ", num,"green bottles hanging on the wall.\n", num,"green bottles hanging on the wall.\nAnd if 1 green bottle should accidentally fall\n")
    num -= 1
    ans = int(input("How many green bottles will be hanging on the wall? "))
    while ans != num:
        ans = int(input("No, try again "))
    print("There will be ", num,"green bottles hanging on the wall\n")
print("There are no more green bottles hanging on the wall")
input("Press enter to continue")
