import sys
from collections import defaultdict
G, Q = defaultdict(list), [("COM", 0)]
for u, v in map(lambda x: x.strip().split(')'), sys.stdin):
    G[u].append(v)
tot = 0
while Q:
    u, d = Q.pop(0)
    tot += d
    Q += [(v, d+1) for v in G[u]]
print(tot)
