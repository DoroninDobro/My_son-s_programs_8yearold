#apend
n1 = eval(input('Number1(>Number2) '))
n2 = eval(input('Number2(<Number1) '))
x = n1+3
NOD = 0
while(NOD != x):
    if    (n1%x == 0 and n2%x == 0):
        NOD = x
    else:
        x = x-1
print(f'NOD={NOD}')
            
    
    
        
