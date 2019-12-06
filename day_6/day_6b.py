import sys
from collections import defaultdict
G, S, Q = defaultdict(list), set(), [("YOU", 0)]
for u, v in map(lambda x: x.strip().split(')'), sys.stdin):
    G[u].append(v)
    G[v].append(u)
while Q:
    u, d = Q.pop(0)
    if u == "SAN":
        break
    if u not in S:
        S.add(u)
        Q += [(v, d+1) for v in G[u]]
print(d-2)
