import random

color1 = random.choice(['r', 'b', 'g', 'w'])
color2 = random.choice(['r', 'b', 'g', 'w'])
color3 = random.choice(['r', 'b', 'g', 'w'])
color4 = random.choice(['r', 'b', 'g', 'w'])

base = 'rgbw'
color = {0: color1, 1: color2, 2: color3, 3: color4}


def usr_input():
    cond1 = True
    while cond1:
        cond1 = True
        while cond1:
            usr_color = input('Please, enter four colors (r,b,g,w) in the order you want: ')
            cond2 = True
            for letter in usr_color:
                if letter not in base:
                    print('The input should only contain rgbw in lowercase')
                    cond2 = False
                    break
            if len(usr_color) != 4:
                print('The input should only contain four letters')
                cond2 = False
            if cond2:
                cond1 = False
    return usr_color


def check_ans(usr_color):
    ex_cond = True
    tmp = {}
    same = 0
    dif = 0
    usr_list = {}
    x = 0
    for letter in usr_color:
        usr_list[x] = letter
        tmp[x] = color[x]
        x = x + 1
    for i in range(0, 4):
        if tmp[i] == usr_list[i]:
            same = same + 1
            usr_list[i] = '0'
            tmp[i] = '1'
    if same == 4:
        ex_cond = False
        return ex_cond
    for i in range(0, 4):
        ltr = usr_list[i]
        for j in range(0, 4):
            if tmp[j] == ltr:
                dif = dif + 1
                usr_list[i] = '0'
                tmp[j] = '1'
    print('Same place: ', same)
    print('Different place: ', dif)
    return ex_cond


def main():
    ex_cond = True
    attempt = 0
    while ex_cond:
        usr_color = usr_input()
        ex_cond = check_ans(usr_color)
        attempt = attempt + 1
    print('\nYou win! You took', attempt, 'attempts, the combination was:', color, '\n')
    input('Press enter to continue... ')
    return


main()
