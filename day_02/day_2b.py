import sys
L = list(map(int, sys.stdin.readline().strip().split(',')))

def test(L, a, b):
    L[1] = a
    L[2] = b
    i = 0
    while L[i] != 99:
        op, j, k, l = L[i:i+4]
        if op == 1:
            L[l] = L[j]+L[k]
        elif op == 2:
            L[l] = L[j]*L[k]
        i += 4
    return L[0]

for a in range(100):
    for b in range(100):
        if test(L[::], a, b) == 19690720:
            print(100*a+b)
