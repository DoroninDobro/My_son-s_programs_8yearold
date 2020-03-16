dfg = [1,]
e = eval(input('num'))
for n in range(2,e):
    num = n
    w = 0
    for v in range(1,n+1):
        d = (num / v)
        if  (num%v) == 0:   
            w += 1
    if    w == 2:
        dfg.append(n) 
print(f'{dfg}')
        
