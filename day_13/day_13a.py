from collections import defaultdict

class IntCode:
    def __init__(self, filename):
        f = open(filename, 'r').readline().strip().split(',')
        self.L = defaultdict(int, list(zip(range(len(f)), map(int, f))))
        self.L[0] = 2
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

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

IC = IntCode("day_13.in")
IC.run()

A = dict()
for a, b, c in list(chunks(IC.out, 3)):
    A[(a, b)] = c

print(sum([1 if v == 2 else 0 for k, v in A.items()]))