name = input("First name (lower case): ")
if len(name) < 5:
    l_name = input("Last name (lower case): ")
    print(str.upper(name+l_name))
else:
    print(str.lower(name))
