from collections import defaultdict

class IntCode:
    def __init__(self, filename):
        f = open(filename, 'r').readline().strip().split(',')
        self.L = defaultdict(int, list(zip(range(len(f)), map(int, f))))
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

IC = IntCode("day_11.in")
IC.inp.append(1)
G, D = defaultdict(int), [(0,1), (1, 0), (0,-1), (-1, 0)]
p, d = (0, 0), 0
while not IC.run():
    G[p] = IC.out.pop(0)
    d = (d+1)%4 if IC.out.pop(0) else (d-1)%4
    p = tuple(sum(t) for t in zip(p, D[d]))
    IC.inp.append(G[p])

x1, y1 = min(x for x,y in G.keys()), max(y for x,y in G.keys())
x2, y2 = max(x for x,y in G.keys()), min(y for x,y in G.keys())
for y in range(y1, y2-1, -1):
    print(''.join(['█' if G[(x, y)] else ' ' for x in range(x1, x2+1)]))
