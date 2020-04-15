def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import numpy as np
N = INT()
A = LIST()

A = np.array(A)

if N % 2 == 0:
    a = A[::2].sum()
    b = A[1::2].sum()
    print(max(a, b))
else:
    a = A[::2].sum()
    b = a - A[-1]
    c = a - A[0]
    d = A[1::2].sum()
    print(max(a, b, c, d))


