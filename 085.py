f_name = input("Enter first name: ")
count = 0
for letter in f_name:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count = count + 1
print(count)

input("\nPress enter to continue")
