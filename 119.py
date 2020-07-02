import random


def get_num():
    low = int(input('Enter a minimum number: '))
    high = int(input('Enter a maximum number: '))
    comp_num = random.randint(low, high)
    return comp_num


def user_ans():
    print('I am thinking of a number… ')
    ans = int(input('Guess the number Im thinking of: '))
    return ans


def check(comp_num, ans):
    while comp_num != ans:
        if ans > comp_num:
            ans = int(input("Too high, guess again: "))
        else:
            ans = int(input("Too low, guess again: "))
    print('Correct, you win!')
    return


def main():
    comp_num = get_num()
    ans = user_ans()
    check(comp_num, ans)
    return


main()
input("\nPress enter to continue")
