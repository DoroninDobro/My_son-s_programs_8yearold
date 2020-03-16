import random
numb = random.randint(1,10)
pop = 0
num = eval(input('num'))
if  num != numb:
    pop = pop + 1
    w = 0
    for v in range(1,numb+1):
        d = (num / v)
        if  (num%v) == 0:   
            w += 1
    if    w == 2:
        print('simple')
    elif  w != 2:
        print('no simple')
elif  num == numb:
    print(f'you win!!! {pop} try')
num = eval(input('num'))
if  num != numb:
    pop = pop + 1
    if  (numb / 3)%1 == 0:
        print('del 3')
    elif  (numb / 3)%1 != 0:
        print('no del 3')
elif  num == numb:
    print(f'you win!!! {pop} try')
num = eval(input('num'))
if  num != numb:
    pop = pop + 1
    if  (numb / 2)%1 == 0:
        print('del 2')
    elif  (numb / 2)%1 != 0:
        print('no del 2')
elif  num == numb:
    print(f'you win:)!!! {pop} try')
elif  num != numb:
    print('you loze:(')

    
