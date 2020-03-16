import MathFunkshions
M = MathFunkshions
m = 0
n = eval(input('num '))
k = eval(input('pop '))
p = eval(input('ver '))
for x in range(k,n+1):
    b = M.numver(p,n,x)
    m = m + b
print(m)
