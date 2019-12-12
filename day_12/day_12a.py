from math import *
from parse import parse

def sgn(x, y):
    return 1 if x < y else (-1 if x > y else 0)

M = [list(map(int, parse("<x={}, y={}, z={}>", input()))) for _ in range(4)]
V = [[0, 0, 0] for _ in range(4)]
for step in range(1000):
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(3):
                V[i][k] += sgn(M[i][k], M[j][k])
                V[j][k] += sgn(M[j][k], M[i][k])
    M = [list(sum(t) for t in zip(M[i], V[i])) for i in range(4)]
print(sum([sum(map(abs, M[i]))*sum(map(abs, V[i])) for i in range(4)]))
