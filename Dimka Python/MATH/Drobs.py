import MathFunkshions
M = MathFunkshions
f = input('funkshion ')
ch1 = eval(input('chislitel 1 '))
zn1 = eval(input('znaminatel 1 '))
ch2 = eval(input('chislitel 2 '))
zn2 = eval(input('znaminatel 2 '))
if  f == '*':
    CH = ch1 * ch2
    ZN = zn1 * zn2
elif  f == '/':
    CH = ch1 * zn2
    ZN = zn1 * ch2
elif  f == '+':
    CH = ch1 + ch2
    ZN = M.NOD(zn1,zn2)
elif  f == '-':
    CH = ch1 - ch2
    ZN = M.NOD(zn1,zn2)
print(f'Chislitel {CH}, Znaminatel {ZN}')
