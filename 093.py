from array import *

num_arr = array('i',[])
for i in range(0,5):
    num_arr.append(int(input("Enter a number: ")))
num_arr = sorted(num_arr)
print(num_arr)
num = int(input("Select the number you want to delete: "))
if num in num_arr:
    num_arr.remove(num)
    num_arr_2 = array('i',[])
    num_arr_2.append(num)
    print(num_arr)
    print(num_arr_2)
else:
    print("The number is not in the array...")


input("\nPress enter to continue")
