#append
F = [1,1]
n = 2
for q in range(10000):
    w = F[n - 1] + F[n - 2]
    F.append(w)
    n = n + 1
Fi = F[n - 1] / F[n - 2]
print(f'Numbers Fibonachi {F} Number Fibonachi {Fi}')
    
