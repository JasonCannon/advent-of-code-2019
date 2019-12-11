a, b = map(int, input().split('-'))
cnt = 0
for n in map(str, range(a, b+1)):
    m = '$'+n+'$'
    if any(m[i] == m[i+1] and m[i] != m[i-1] and m[i+1] != m[i+2] for i in range(1, len(m)-2)) and all(x <= y for x, y in zip(n, n[1:])):
        cnt += 1
print(cnt)
