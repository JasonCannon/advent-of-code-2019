s, n = input(), 25*6
mn = (float("inf"), 0)
for i in range(len(s)//n):
    l = s[n*i:n*(i+1)]
    mn = min(mn, (l.count('0'), l.count('1')*l.count('2')))
print(mn[1])
