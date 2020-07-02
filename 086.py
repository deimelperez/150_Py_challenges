pass_1 = input("Enter new password: ")
pass_2 = input("Re-enter password: ")
if pass_1 == pass_2:
    print("Thanks")
elif pass_1.lower() == pass_2.lower():
    print("They must be in the same case")
else:
    print("Incorrect")

input("\nPress enter to continue")
