foods = {}
for i in range(1,5):
    foods[i] = input("Enter a food: ")
print(foods)
ch = int(input("Which one do you want to get rid of? "))
del foods[ch]
print(sorted(foods.values()))


input("Press enter to continue")
