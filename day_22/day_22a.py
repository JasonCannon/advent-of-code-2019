import sys
C = list(range(10007))
for L in map(lambda x : x.split(), sys.stdin):
    if L[0] == 'deal' and L[1] == 'with':
        n = int(L[3])
        D = [None]*len(C)
        for i in range(len(C)):
            D[n*i%len(D)] = C[i]
    elif L[0] == 'deal' and L[1] == 'into':
        D = C[::-1]
    elif L[0] == 'cut':
        n = int(L[1])
        D = C[n:] + C[:n]
    C = D
print(C.index(2019))
