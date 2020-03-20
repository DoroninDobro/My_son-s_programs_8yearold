import MathFunkshions as M

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
    ZN = M.NOK(zn1,zn2)
    CH = (ch1 * (ZN / zn1)) + (ch2 * (ZN / zn2))
elif  f == '-':
    ZN = M.NOK(zn1,zn2)
    CH = (ch1 * (ZN / zn1)) - (ch2 * (ZN / zn2))
DR = M.skrdrob(CH,ZN)
CH = DR[0]
ZN = DR[1]
print(f'Chislitel {CH}, Znaminatel {ZN}')
