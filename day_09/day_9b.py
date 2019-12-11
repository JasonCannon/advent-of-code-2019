from collections import defaultdict
L = input().strip().split(',')
L = defaultdict(int, list(zip(range(len(L)), map(int, L))))
i, rel_base = 0, 0

def m_get(j, p):
    global rel_base
    if p == 0:
        return L[j]
    elif p == 1:
        return j
    elif p == 2:
        return L[rel_base+j]

def m_set(j, p):
    global rel_base
    if p == 0 or p == 1:
        return j
    elif p == 2:
        return rel_base+j

while L[i] != 99:
    I = str(L[i]).rjust(5, '0')
    i += 1
    op = int(I[-2:])
    p1, p2, p3 = map(int, I[-3:-6:-1])
    # Handle ops
    if op == 1:
        L[m_set(L[i+2], p3)] = m_get(L[i], p1) + m_get(L[i+1], p2)
        i += 3
    elif op == 2:
        L[m_set(L[i+2], p3)] = m_get(L[i], p1) * m_get(L[i+1], p2)
        i += 3
    elif op == 3:
        L[m_set(L[i], p1)] = int(input())
        i += 1
    elif op == 4:
        print(m_get(L[i], p1))
        i += 1
    elif op == 5:
        if m_get(L[i], p1):
            i = m_get(L[i+1], p2)
        else:
            i += 2
    elif op == 6:
        if not m_get(L[i], p1):
            i = m_get(L[i+1], p2)
        else:
            i += 2
    elif op == 7:
        L[m_set(L[i+2], p3)] = (1 if m_get(L[i], p1) < m_get(L[i+1], p2) else 0)
        i += 3
    elif op == 8:
        L[m_set(L[i+2], p3)] = (1 if m_get(L[i], p1) == m_get(L[i+1], p2) else 0)
        i += 3
    elif op == 9:
        rel_base += m_get(L[i], p1)
        i += 1
