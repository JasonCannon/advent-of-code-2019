import sys

def get_fuel(n):
    return max(n//3-2, 0)

sm = 0
for n in map(int, sys.stdin):
    while get_fuel(n):
        n = get_fuel(n)
        sm += n
print(sm)
