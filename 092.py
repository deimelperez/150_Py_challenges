from array import *
import random

num_arr = array('i',[])
for i in range(0,5):
    num_arr.append(random.randint(1,1000))

num_arr_usr = array('i',[])
for i in range(0,3):
    num_arr_usr.append(int(input("Enter a number: ")))


num_arr.extend(num_arr_usr)
num_arr = sorted(num_arr)
for i in num_arr:
    print(i)



input("\nPress enter to continue")
