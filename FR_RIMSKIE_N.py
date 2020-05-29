def FRRIM(l):
    n = list(l)
    w = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    o = 0
    k = w[n[len(n)-1]]
    o += k
    for h in range(len(n)-2, -1, -1):
        if w[n[h]]>=k:
            o += w[n[h]]
        else:
            o -= w[n[h]]
    return o

n = input('Введите римское число и узрейте силу программирования: ')
print(TORIM(n))
        
        
        
