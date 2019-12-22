import sys
D = 119315717514047
N = 101741582076661
L = [line.split() for line in sys.stdin]

def euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    d, x, y = euclidean(b%a, a)
    return (d, (y-(b//a)*x), x)

def process(idx):
    for l in L[::-1]:
        if l[0] == 'deal' and l[1] == 'with':
            n = int(l[3])
            idx = (idx*euclidean(n, D)[1])%D
        elif l[0] == 'deal' and l[1] == 'into':
            idx = D-idx-1
        elif l[0] == 'cut':
            n = int(l[1])
            idx = (idx+n)%D
    return idx%D

pos1 = 2020
pos2 = process(pos1)
pos3 = process(pos2)
A = ((pos2-pos3)*euclidean((pos1-pos2)%D, D)[1])%D
B = (pos2-pos1*A)%D
print((pow(A, N, D)*pos1 + (pow(A, N, D)-1)*euclidean(A-1, D)[1]*B)%D)
