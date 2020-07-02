nums = []
for i in range(0,3):
    nums.append(int(input("Enter number: ")))
    print(nums)
ch = input("Do you want the las number? (y/n): ")
if ch == "n":
    del nums[len(nums)-1]
print(nums)

input("Press enter to continue")
