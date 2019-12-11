s, n = input(), 25*6
L = ['2']*n
for i in range(len(s)//n):
    L = [i if i != '2' else j for i, j in zip(L, s[n*i:n*(i+1)])]
print('\n'.join([''.join(' ' if j == '0' else '#' for j in L[25*i:25*(i+1)]) for i in range(6)]))
