import math
A, B, X = map(int, input().split())


def d (N):
    return int(math.log10(N))+1

if X//A == 0 or X//B==0 or A*1+B*d(1) > X:
    print(0)
    exit()



if A >= B:
    n = X // B
else:
    n = X // A

while A*n+B*d(n) > X:
    sum = 
    n -= 1

print(min(n, 10**9))