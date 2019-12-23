from collections import defaultdict
from copy import copy

class IntCode:
    def __init__(self, filename, mode = None):
        f = open(filename, 'r').readline().strip().split(',')
        self.__tape = defaultdict(int, list(zip(range(len(f)), map(int, f))))
        if mode: self.__tape[0] = mode
        self.reset()

    def reset(self):
        self.L = copy(self.__tape)
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

n, C = 50, []

for i in range(50):
    C.append(IntCode("day_23.in"))
    C[i].inp.append(i)
    C[i].run()

while True:
    Q = defaultdict(list)
    for i in range(50):
        while C[i].out:
            d, x, y = C[i].out[:3]
            del C[i].out[:3]
            Q[d] += [x, y]
    if 255 in Q:
        break
    for i in range(50):
        C[i].inp += Q.get(i, [-1])
        C[i].run()

print(Q[255][-1])
