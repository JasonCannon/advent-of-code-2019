inp = input()
offset = int(inp[:7])
L = list(map(int, inp))*10000

for _ in range(100):
    sm = sum(L[i] for i in range(offset, len(L)))
    for i in range(offset, len(L)):
        sm_i = sm
        sm -= L[i]
        L[i] = sm_i%10

print(''.join(map(str, L[offset:offset+8])))
