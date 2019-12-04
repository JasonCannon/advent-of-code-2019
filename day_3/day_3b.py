D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
def get_path():
    p = (0, 0)
    s = 0
    for step in input().split(','):
        for i in range(int(step[1:])):
            p = tuple(map(sum, zip(p, D[step[0]])))
            s += 1
            yield (*p, s)
P = dict()
for x, y, s in get_path():
    if (x, y) not in P:
        P[(x, y)] = s
print(min(s+P[(x, y)] for x, y, s in get_path() if (x, y) in P))
