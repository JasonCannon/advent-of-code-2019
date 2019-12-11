import sys
from math import *
from collections import defaultdict

S, D = [], defaultdict(list)

for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        if c == '#':
            S.append((x, y))
_, p = max([(len(set([atan2(y2-y1, x2-x1) for x2, y2 in S])), (x1, y1)) for x1, y1 in S])

for q in S:
    if q != p:
        D[(atan2(q[1]-p[1], q[0]-p[0])+pi/2)%(2*pi)].append(q)

L = [sorted(v, key = lambda q : hypot(q[0]-p[0], q[1]-p[1])) for k, v in sorted(D.items())]
for _ in range(200):
    q = L[0].pop(0)
    if not L[0]:
        L.pop(0)
    else:
        L.append(L.pop(0))

print(100*q[0]+q[1])
