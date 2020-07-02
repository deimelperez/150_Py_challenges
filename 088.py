from array import *

num_arr = array('i',[])
for i in range(0,5):
    num_arr.append(int(input("Enter a number: ")))
num_arr = sorted(num_arr)
num_arr.reverse()
print(num_arr)

input("\nPress enter to continue")
