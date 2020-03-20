x = 12
y = 6
w = y
NOK = -45
while  NOK != w:
    if  w%y == 0 and w%x == 0:
        NOK = w
    else:
        w = w + y
print(f'{NOK}')
        
