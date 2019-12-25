from copy import deepcopy
G = tuple(tuple(input()) for _ in range(5))

def adj(A, r, c):
    cnt = 0
    return sum(A[r+dr][c+dc] == '#' for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)] if 0 <= r+dr < 5 and 0 <= c+dc < 5)

def update(A):
    B = [list(a) for a in A]
    for r in range(5):
        for c in range(5):
            if A[r][c] == '#' and adj(A, r, c) != 1:
                B[r][c] = '.'
            elif A[r][c] == '.' and adj(A, r, c) in {1, 2}:
                B[r][c] = '#'
    return tuple(tuple(b) for b in B)

seen = set()
while G not in seen:
    seen.add(G)
    G = update(G)
print(sum(2**(5*r+c) for c in range(5) for r in range(5) if G[r][c] == '#'))

