from array import *
import random

num_arr = array('i',[])
for i in range(0,5):
    num_arr.append(random.randint(1,1000))
print(num_arr)
num = int(input("Select a number: "))
while not num in num_arr:
     num = int(input("Try again: "))
print("The index of the selected number is", num_arr.index(num))

input("\nPress enter to continue")
