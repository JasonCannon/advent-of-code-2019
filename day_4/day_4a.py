a, b = map(int, input().split('-'))
cnt = 0
for n in map(str, range(a, b+1)):
    if any(x == y for x, y in zip(n, n[1:])) and all(x <= y for x, y in zip(n, n[1:])):
        cnt += 1
print(cnt)
