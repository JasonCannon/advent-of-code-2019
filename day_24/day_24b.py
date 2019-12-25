from copy import deepcopy
G = [[list(".....") for j in range(5)] for i in range(250)]
G[0] = [list(input()) for j in range(5)]
# for i in range(len(G)): G[i][2][2] = '?'

def neighbours(layer, r, c):
    cnt = 0
    if r == 0 and G[layer-1][1][2] == '#': cnt += 1
    if r == 4 and G[layer-1][3][2] == '#': cnt += 1
    if c == 0 and G[layer-1][2][1] == '#': cnt += 1
    if c == 4 and G[layer-1][2][3] == '#': cnt += 1
    if (r, c) == (1, 2): cnt += sum(G[layer+1][0][dc] == '#' for dc in range(5))
    if (r, c) == (2, 1): cnt += sum(G[layer+1][dr][0] == '#' for dr in range(5))
    if (r, c) == (2, 3): cnt += sum(G[layer+1][dr][4] == '#' for dr in range(5))
    if (r, c) == (3, 2): cnt += sum(G[layer+1][4][dc] == '#' for dc in range(5))
    return cnt + sum(G[layer][r+dr][c+dc] == '#' for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)] if 0 <= r+dr < 5 and 0 <= c+dc < 5 and (r+dr, c+dc) != (2, 2))

def update(layer):
    for r in range(5):
        for c in range(5):
            if (r, c) == (2, 2): continue
            cnt = neighbours(layer, r, c)
            if G[layer][r][c] == '#' and cnt != 1:
                A[layer][r][c] = '.'
            elif G[layer][r][c] == '.' and cnt in {1, 2}:
                A[layer][r][c] = '#'

for i in range(200):
    A = deepcopy(G)
    for layer in range(-(i+1), i+2): update(layer)
    G = A

print(sum(G[l][r][c] == '#' for c in range(5) for r in range(5) for l in range(len(G))))
