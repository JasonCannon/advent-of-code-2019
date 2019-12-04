import sys

sm = 0
for n in map(int, sys.stdin):
    sm += n//3 - 2
print(sm)
