L = list(map(int, input().strip().split(',')))
i = 0

def m(j, p):
    return L[j] if not p else j

while L[i] != 99:
    I = str(L[i]).rjust(5, '0')
    i += 1
    op = int(I[-2:])
    p1, p2, p3 = map(int, I[-3:-6:-1])
    # Handle ops
    if op == 1:
        L[L[i+2]] = m(L[i], p1) + m(L[i+1], p2)
        i += 3
    elif op == 2:
        L[L[i+2]] = m(L[i], p1) * m(L[i+1], p2)
        i += 3
    elif op == 3:
        L[L[i]] = int(input())
        i += 1
    elif op == 4:
        print(m(L[i], p1))
        i += 1
    elif op == 5:
        if m(L[i], p1):
            i = m(L[i+1], p2)
        else:
            i += 2
    elif op == 6:
        if not m(L[i], p1):
            i = m(L[i+1], p2)
        else:
            i += 2
    elif op == 7:
        L[L[i+2]] = (1 if m(L[i], p1) < m(L[i+1], p2) else 0)
        i += 3
    elif op == 8:
        L[L[i+2]] = (1 if m(L[i], p1) == m(L[i+1], p2) else 0)
        i += 3
