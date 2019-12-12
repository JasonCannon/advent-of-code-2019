from math import *
from parse import parse
from functools import reduce

def sgn(x, y):
    return 1 if x < y else (-1 if x > y else 0)

def lcm(a, b):
    return a*b//gcd(a, b)

def solve(A):
    B, V = A[::], [0, 0, 0, 0]
    step = 0
    while True:
        step += 1
        for i in range(4):
            for j in range(i+1, 4):
                V[i] += sgn(B[i], B[j])
                V[j] += sgn(B[j], B[i])
        B = [B[i]+V[i] for i in range(4)]
        if A == B and all([v == 0 for v in V]):
            return step

M = [list(map(int, parse("<x={}, y={}, z={}>", input()))) for _ in range(4)]
print(reduce(lcm, [solve(list(list(zip(*M))[i])) for i in range(3)]))
