L = list(map(int, input()))
C, patt = [[] for _ in range(len(L))], [0, 1, 0, -1]
for i in range(len(L)):
    for p in patt:
        C[i] += [p]*(i+1)

for _ in range(100):
    for i in range(len(L)):
        L[i] = abs(sum(L[j]*C[i][(j+1)%len(C[i])] for j in range(len(L))))%10

print(''.join(map(str, L[:8])))
