from array import *

num_arr = array('i',[])
count = 0
while count < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num > 10 and num < 20:
        num_arr.append(num)
        count += 1
    else:
        print("Try again...\n")
for i in num_arr:
    print(i)

input("\nPress enter to continue")
