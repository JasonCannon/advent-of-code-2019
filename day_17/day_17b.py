from collections import defaultdict
from itertools import product

class IntCode:
    def __init__(self, filename, mode = None):
        f = open(filename, 'r').readline().strip().split(',')
        self.L = defaultdict(int, list(zip(range(len(f)), map(int, f))))
        if mode: self.L[0] = mode
        self.i, self.rel_base = 0, 0
        self.inp, self.out = [], []

    def m_get(self, j, p):
        if p == 0:
            return self.L[j]
        elif p == 1:
            return j
        elif p == 2:
            return self.L[self.rel_base+j]

    def m_set(self, j, p):
        if p == 0 or p == 1:
            return j
        elif p == 2:
            return self.rel_base+j

    def run(self):
        while self.L[self.i] != 99:
            I = str(self.L[self.i]).rjust(5, '0')
            self.i += 1
            op = int(I[-2:])
            p1, p2, p3 = map(int, I[-3:-6:-1])
            # Handle ops
            if op == 1:
                self.L[self.m_set(self.L[self.i+2], p3)] = self.m_get(self.L[self.i], p1) + self.m_get(self.L[self.i+1], p2)
                self.i += 3
            elif op == 2:
                self.L[self.m_set(self.L[self.i+2], p3)] = self.m_get(self.L[self.i], p1) * self.m_get(self.L[self.i+1], p2)
                self.i += 3
            elif op == 3:
                if not self.inp:
                    self.i -= 1
                    return False
                self.L[self.m_set(self.L[self.i], p1)] = int(self.inp.pop(0))
                self.i += 1
            elif op == 4:
                self.out.append(self.m_get(self.L[self.i], p1))
                self.i += 1
            elif op == 5:
                if self.m_get(self.L[self.i], p1):
                    self.i = self.m_get(self.L[self.i+1], p2)
                else:
                    self.i += 2
            elif op == 6:
                if not self.m_get(self.L[self.i], p1):
                    self.i = self.m_get(self.L[self.i+1], p2)
                else:
                    self.i += 2
            elif op == 7:
                self.L[self.m_set(self.L[self.i+2], p3)] = (1 if self.m_get(self.L[self.i], p1) < self.m_get(self.L[self.i+1], p2) else 0)
                self.i += 3
            elif op == 8:
                self.L[self.m_set(self.L[self.i+2], p3)] = (1 if self.m_get(self.L[self.i], p1) == self.m_get(self.L[self.i+1], p2) else 0)
                self.i += 3
            elif op == 9:
                self.rel_base += self.m_get(self.L[self.i], p1)
                self.i += 1
        return True

IC = IntCode("day_17.in")
IC.run()
G = list(map(lambda x : list(x), ''.join(chr(x)for x in IC.out).strip().split()))
tiles = 0

def in_bounds(dy, dx):
    return dy >= 0 and dy < len(G) and dx >= 0 and dx < len(G[0])

for r in range(len(G)):
    for c in range(len(G[r])):
        if G[r][c] == '#':
            tiles += 1
        elif G[r][c] in {'^', 'v', '<', '>'}:
            y, x, dr = r, c, G[r][c]

seq = []
seen = set()
D = {'^':[('<', 'L', 0, -1), ('>', 'R', 0, 1)], 'v':[('<', 'R', 0, -1), ('>', 'L', 0, 1)], '<':[('^', 'R', -1, 0), ('v', 'L', 1, 0)], '>':[('^', 'L', -1, 0), ('v', 'R', 1, 0)]}

while len(seen) < tiles:
    for ddr, s, _y, _x in D[dr]:
        dy, dx, cnt = y, x, 0
        while in_bounds(dy+_y, dx+_x) and G[dy+_y][dx+_x] == '#':
            dy, dx = dy+_y, dx+_x
            seen.add((dy, dx))
            cnt += 1
        if cnt:
            y, x, dr = dy, dx, ddr
            seq += [s, cnt]
            break

def get_matches(L, P):
    i = 0
    while i <= len(L)-len(P):
        if L[i:i+len(P)] == P:
            yield (i, i+len(P))
            i += len(P)
        else: i += 1

def has_overlap(A, B):
    return any([max(a[0], b[0]) <= min(a[1], b[1]) for a in A for b in B])

i, prefixes = 2, [[seq[0], seq[1]]]
while i < len(seq):
    L = prefixes[-1]+[seq[i], seq[i+1]]
    if len(','.join(map(str, L))) > 20:
        break
    prefixes.append(L)
    i += 2

i, suffixes = len(seq)-3, [[seq[-2], seq[-1]]]
while i > 0:
    L = [seq[i-1], seq[i]]+suffixes[-1]
    if len(','.join(map(str, L))) > 20:
        break
    suffixes.append(L)
    i -= 2

for P, S in product(prefixes, suffixes):
    X, Z = list(get_matches(seq, P)), list(get_matches(seq, S))
    if has_overlap(X, Z):
        continue
    V = list(sorted(X+Z))
    L = [seq[V[i-1][1]:V[i][0]] for i in range(1, len(V)) if seq[V[i-1][1]:V[i][0]]]
    if all(L[i-1] == L[i] for i in range(1, len(L))) and len(','.join(map(str, L[0]))) <= 20:
        Y = [(V[i-1][1], V[i][0]) for i in range(1, len(V)) if seq[V[i-1][1]:V[i][0]]]
        X, Y, Z = list(map(lambda x:(x, 'A'), X)), list(map(lambda y:(y, 'B'), Y)), list(map(lambda z:(z, 'C'), Z))
        M = ','.join(map(lambda x:x[1], sorted(X+Y+Z)))
        A, B, C = ','.join(map(str, P)), ','.join(map(str, L[0])), ','.join(map(str, S))

IC = IntCode("day_17.in", mode=2)
IC.inp = [ord(c) for c in M+'\n'+A+'\n'+B+'\n'+C+"\nn\n"]
IC.run()
print(IC.out[-1])