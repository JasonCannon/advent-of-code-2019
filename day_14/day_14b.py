import sys
from collections import defaultdict

G = dict()
for line in map(lambda x: list(map(lambda y: y.strip(), x.split('=>'))), sys.stdin):
    a, b = [x.strip().split(' ') for x in line[0].split(',')], line[1].split(' ')
    G[b[1]] = (int(b[0]), tuple((int(x), y) for x, y in a))

def get_ore(amt):
    Q, C = defaultdict(int, {'FUEL': amt}), defaultdict(int)
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
    return cnt

lo, hi = 1, 1
while get_ore(hi) < 1e12:
    hi *= 2

while lo < hi-1:
    mi = (lo+hi)//2
    amt = get_ore(mi)
    if amt < 1e12:
        lo = mi
    elif amt > 1e12:
        hi = mi
    else:
        break
print(hi if get_ore(hi) <= 1e12 else lo)