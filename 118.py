def get_num():
    num = int(input('Enter a number: '))
    return num
    
def print_count(num):
    for i in range(1,num + 1):
        print(i)
    return
    
def main():
    num = get_num()
    print_count(num)
    return
    
main()
input("\nPress enter to continue")
