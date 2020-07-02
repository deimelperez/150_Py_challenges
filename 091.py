from array import *

num_arr = array('i',[2,34,2,14,65,2,14])
print(num_arr)
num = int(input("Enter a number from the array: "))
print(num,"is repeated", num_arr.count(num),"times")

input("\nPress enter to continue")
