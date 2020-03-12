def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
P = LIST()
Q = LIST()

import itertools

for i, l in enumerate(itertools.permutations(range(1, N+1), N)):
    if list(l) == P:
        a = i+1
    if list(l) == Q:
        b = i+1

print(abs(a-b))