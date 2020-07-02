from array import *
import random

num_arr = array('i',[])
for i in range(0,5):
    num_arr.append(random.randint(1,1000))
for i in num_arr:
    print(i)

input("\nPress enter to continue")
