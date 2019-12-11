import sys
from math import *
S, mx = [], 0
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        if c == '#':
            S.append((x, y))
print(max([len(set([atan2(y2-y1, x2-x1) for x2, y2 in S])) for x1, y1 in S]))