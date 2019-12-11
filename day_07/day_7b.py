from itertools import permutations 

init = list(map(int, open("day_7.in", 'r').readline().strip().split(',')))
mx = 0

for perm in permutations(range(5, 10)):
    Alive = [True]*5
    Ls = [init[::] for i in range(5)]
    Is = [0]*5
    Inps = [[p] for p in perm]
    Inps[0].append(0)

    def run(id, L, inp, i):
        def m(j, p):
            return L[j] if not p else j

        while True:
            if L[i] == 99:
                Alive[id] = False
                break
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
                if not inp:
                    i -= 1
                    break
                L[L[i]] = inp.pop(0)
                i += 1
            elif op == 4:
                Inps[(id+1)%5].append(m(L[i], p1))
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
        Is[id] = i 

    while any(Alive):
        for i in range(5):
            run(i, Ls[i], Inps[i], Is[i])

    mx = max(mx, Inps[0][0])

print(mx)