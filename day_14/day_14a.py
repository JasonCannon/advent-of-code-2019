import sys
from collections import defaultdict

G = dict()
for line in map(lambda x: list(map(lambda y: y.strip(), x.split('=>'))), sys.stdin):
    a, b = [x.strip().split(' ') for x in line[0].split(',')], line[1].split(' ')
    G[b[1]] = (int(b[0]), tuple((int(x), y) for x, y in a))

Q, C = defaultdict(int, {'FUEL': 1}), defaultdict(int)
cnt = 0
while Q:
    u, n = next(iter(Q.items()))
    m, a = G[u]
    q, r = divmod(n, m)
    del Q[u]
    if r:
        C[u] = m - r
        q += 1
    for x, y in a:
        if y == 'ORE':
            cnt += q*x-C[y]
        else:
            Q[y] += q*x-C[y]
            del C[y]
print(cnt)