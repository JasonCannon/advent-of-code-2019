import sys
from heapq import *
from collections import defaultdict

M = [list(line.rstrip('\n')) for line in sys.stdin]
A = defaultdict(list)
for i in range(2, len(M)-2):
    for j in range(2, len(M[i])-2):
        if M[i][j] == '.':
            for s in [M[i][j-2]+M[i][j-1], M[i][j+1]+M[i][j+2], M[i-2][j]+M[i-1][j], M[i+1][j]+M[i+2][j]]:
                if s.isalpha():
                    A[s].append((i, j))
W = dict()
for l in filter(lambda x: len(x) > 1, A.values()):
    W[l[0]] = l[1]
    W[l[1]] = l[0]

Y, X = [-1, 0, 1, 0], [0, 1, 0, -1]
Q = [(0, *A["AA"])]
dist = dict()
while Q:
    t, p = heappop(Q)
    if p in dist:
        continue
    dist[p] = t
    if p == A["ZZ"][0]:
        print(t)
        break
    if p in W:
        heappush(Q, (t+1, W[p]))
    for i in range(4):
        dy, dx = p[0]+Y[i], p[1]+X[i]
        if M[dy][dx] == '.':
            heappush(Q, (t+1, (dy, dx)))
