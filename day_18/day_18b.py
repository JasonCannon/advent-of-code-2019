import sys
from heapq import *

M, D = [list(line.strip()) for line in sys.stdin], dict()
Y, X = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = ord('0')
for r in range(len(M)):
    for c in range(len(M[r])):
        if M[r][c].islower():
            D[M[r][c]] = (r, c)
        elif M[r][c] == '@':
            D[chr(cnt)] = (r, c)
            cnt += 1
keys = len(D.keys())-(cnt-ord('0'))

def bfs(p):
    Q = [(*p, 0, ())]
    S, K = set(), dict()
    while Q:
        y, x, t, D = Q.pop(0)
        if (y, x) in S:
            continue
        S.add((y, x))
        if M[y][x].islower() and p != (y, x):
            K[M[y][x]] = (t, frozenset(D))
        for i in range(4):
            dy, dx = y+Y[i], x+X[i]
            if M[dy][dx] != '#':
                Q.append((dy, dx, t+1, D+(M[dy][dx].lower(),) if M[dy][dx].isupper() else D))
    return K

G = {c:dict() for c in D.keys()}
for c in D.keys():
    for k, v in bfs(D[c]).items():
        G[c][k] = v

Q = [(0, (('0', '1', '2', '3'), frozenset()))]
dist = dict()
while Q:
    d, node = heappop(Q)
    if node in dist:
        continue
    dist[node] = d
    U, S = node
    if len(S) == keys:
        print(d)
        break
    for i in range(len(U)):
        for v, (w, T) in G[U[i]].items():
            if len(T-S) == 0 and v not in S:
                heappush(Q, ((d+w), (U[:i]+(v,)+U[i+1:], S|frozenset(v))))
