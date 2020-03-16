num = 1
while num != 0:
    num = int(input('number or 0 to exit '))
    w = 0
    for n in range(num, 0, -1):
        d = (num / n)
        if  (d%1) == 0:   
            w += 1
    if    w > 2:
        print(f'Не простое и количество делителей {w}')
    else:
        print('Простое')
