countries = ("cuba","eeuu","china","spain","russia")
for i in countries:
    print(i)
ch = input("Enter a country: ")
print(countries.index(ch))
ch = int(input("\nEnter a number(0-4): "))
print(countries[ch])

input("Press enter to continue")
