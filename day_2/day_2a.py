import sys
L = list(map(int, sys.stdin.readline().strip().split(',')))
L[1] = 12
L[2] = 2
i = 0
while L[i] != 99:
    op, j, k, l = L[i:i+4]
    if op == 1:
        L[l] = L[j]+L[k]
    elif op == 2:
        L[l] = L[j]*L[k]
    i += 4
print(L[0])
