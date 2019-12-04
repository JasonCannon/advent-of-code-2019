D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
def get_path():
    p = (0, 0)
    for step in input().split(','):
        for i in range(int(step[1:])):
            p = tuple(map(sum, zip(p, D[step[0]])))
            yield p
P = set(get_path())
print(min(abs(x)+abs(y) for x, y in get_path() if (x, y) in P))
