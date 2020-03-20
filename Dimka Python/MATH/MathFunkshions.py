#return
#append
def fibnum():
    F = [1,1]
    n = 2
    for q in range(5000):
        w = F[n - 1] + F[n - 2]
        F.append(w)
        n = n + 1
    Fi = F[n - 1] / F[n - 2]
    return Fi

def fibnums(u):
    F = [1,1]
    n = 2
    for q in range(5000):
        w = F[n - 1] + F[n - 2]
        F.append(w)
        n = n + 1
    Fi = F[n - 1] / F[n - 2]
    return F[u-1]


def simpnums(g):
    dfg = [1,]
    for n in range(2,1200):
        num = n
        w = 0
        for v in range(1,n+1):
            d = (num / v)
            if  (num%v) == 0:   
                w += 1
        if    w == 2:
            dfg.append(n)
    return dfg[g]

def faktor(x):
    z = []
    r = 1
    for t in range(1,x + 1):
        z.append(t)
        r = r * t
    return r

def modl(t):
    n = t
    if  n < 0:
        Modulle = n - n - n 
    elif  n == 0:
        Modulle = 0
    elif  n > 0:
        Modulle = n
    return Modulle

def numsoch(k,n):
    x = faktor(n)
    y = faktor(n - k)
    z = faktor(k)
    r = y * z
    f = x / r
    return f

def e():
    return 2,7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680

def bernPHE(PH,PE,PHE):
    return PHE*PE/PH

def numver(p,n,k):
    q = n - k
    r = (1 - p) ** q
    y = p ** k
    u = numsoch(k,n)
    P = r * y * u
    return P

def dgeta(r):
    u = 1 / (1 ** r)
    for n in range(2,100000):
        u = u + (1 / (n ** r))
    return u

def stcor(z,x):
    r = z ** (1 / x)
    return r

def pi():
    return 3.141592

def numrazb(n):
    x = 4 * n * stcor(3,2)
    e = 2.72
    p = pi()
    f = p * stcor(2 * n / 3,2)
    h = e ** f
    r = (1 / x) * h
    return r

def NOD(n1,n2):
    x = n1+3
    NOD = 0
    while(NOD != x):
        if    (n1%x == 0 and n2%x == 0):
            NOD = x
        else:
            x = x-1
    return NOD

def delit(x):
    dl = []
    for r in range(1,x+1):
        if  (x / r)%1 == 0:
            dl.append(r)
    return dl

def drobmno(ch1,zn1,ch2,zn2):
    CH = ch1 * ch2
    ZN = zn1 * zn2
    r = [CH,ZN]
    return r

def drobdel(ch1,zn1,ch2,zn2):
    CH = ch1 * zn2
    ZN = zn1 * ch2
    r = [CH,ZN]
    return r

def drobplst(ch1,zn1,ch2,zn2):
    CH = ch1 + ch2
    ZN = NOD(zn1,zn2)
    r = [CH,ZN]
    return r

def drobmins(ch1,zn1,ch2,zn2):
    CH = ch1 - ch2
    ZN = NOD(zn1,zn2)
    r = [CH,ZN]
    return r

def delnum(num):
    w = []
    for n in range(num, 0, -1):
        d = (num / n)
        if  (d%1) == 0:   
            w.append(n)
    return w

def dellen(num):
    w = []
    for n in range(num, 0, -1):
        d = (num / n)
        if  (d%1) == 0:   
            w.append(n)
    return len(w)

def skrdrob(ch,zn):
    CH = ch / NOD(ch,zn)
    ZN = zn / NOD(ch,zn)
    D = [CH,ZN]
    return D

def NOK(x,y):
    w = y
    NOK = -45
    while  NOK != w:
        if  w%y == 0 and w%x == 0:
            NOK = w
        else:
            w = w + y
    return NOK

def ery(x,y):
    g = 1
    w = []
    h = y
    r = 0
    while  h > 0.1:
        w.append(h%x)
        h = round(h / x)
    e = len(w)
    for v in range(e-1,0,-1):
        j = (10 ** v) * w[v]
        r = r + j
    return r

f = ery(2,456)
print(f)
        
        
        
        
        
    

    





    

    
    





