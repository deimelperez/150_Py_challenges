from array import *
import math

num_arr = array('f',[52.34,22.14,65.20,78.14])

num = int(input("Enter a number between 2 and 5: "))
while num < 2 or num > 5:
     num = int(input("Try again: "))
for i in range(0,len(num_arr)):
    ans = num_arr[i]/num
    print(round(ans,2))

input("\nPress enter to continue")
