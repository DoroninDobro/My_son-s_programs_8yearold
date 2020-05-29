def IX(n):
    w = []
    if n<4:
        for v in range(1, n+1):
            w.append('I')
    elif n<=5:
        for v in range(1, 6-n):
            w.append('I')
        w.append('V')
    elif n>5 and n<9:
        w.append('V')
        for v in range(1, n-4):
            w.append('I')
    elif n<=10:
        for v in range(1, 11-n):
            w.append('I')
        w.append('X')
    if len(w)>1:
        return ''.join(w)
    else :
        return w[0]
    
def IC(m):
    n = m//10
    w = []
    if n<4:
        for v in range(1, n+1):
            w.append('X')
    elif n<=5:
        for v in range(1, 6-n):
            w.append('X')
        w.append('L')
    elif n>5 and n<9:
        w.append('L')
        for v in range(1, n-4):
            w.append('X')
    elif n<=10:
        for v in range(1, 11-n):
            w.append('X')
        w.append('C')
    if m%10 != 0:
        w.append(IX(m%10))
    if len(w)>1:
        return ''.join(w)
    else :
        return w[0]                             
    
def IM(m):
    n = m//100
    k = []
    if n<4:
        for v in range(1, n+1):
            k.append('C')
    elif n<=5:
        for v in range(1, 6-n):
            k.append('C')
        k.append('D')
    elif n>5 and n<9:
        k.append('D')
        for v in range(1, n-4):
            k.append('C')
    elif n<=10:
        for v in range(1, 11-n):
            k.append('C')
        k.append('M')
    if m%100 != 0:
        k.append(IC(m%100))
    if len(k)>1:
        return ''.join(k)
    else :
        return k[0]

def TORIM(n):
    if n <= 10:
        return IX(n)
    elif n <= 100:
        return IC(n)
    else:
        return IM(n)


# n = int(input())
print(RIMS(int(input('Введите число: '))))
    

