w = []
b = '0'
n = eval(input('len '))
for x in range(n):
    b = input('bukv or exit ')
    if  b == 'a':
        w.append('!')
    if  b == 'b':
        w.append('*')
    if  b == 'c':
        w.append('?')
    if  b == 'd':
        w.append('#')
    if  b == 'e':
        w.append('"')
    if  b == 'f':
        w.append('`')
    if  b == 'g':
        w.append(':')
    if  b == 'h':
        w.append(';')
    if  b == 'i':
        w.append('.')
    if  b == 'j':
        w.append('@')
    if  b == 'l':
        w.append('&')
    if  b == 'm':
        w.append('^')
    if  b == 'n':
        w.append('-')
    if  b == 'o':
        w.append('=')
    if  b == 'p':
        w.append('+')
    if  b == 'q':
        w.append('/')
    if  b == 'r':
        w.append('|')
    if  b == 's':
        w.append('%')
    if  b == 't':
        w.append('(')
    if  b == 'u':
        w.append(')') 
    if  b == 'v':
        w.append(',')
    if  b == 'w':
        w.append('~')
    if  b == 'x':
        w.append('_')
    if  b == 'y':
        w.append('{')
    if  b == 'z':
        w.append('}')
    if  b == ' ':
        w.append('  ')
for h in range(n):
    m = w[h]
    print(f'{m}')

    
    
    
