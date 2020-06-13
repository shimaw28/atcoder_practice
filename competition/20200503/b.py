def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()

s = [0] * N
d, A = [], []
for i in range(K):
    d = INT()
    ai = LIST()
    for aii in ai:
        s[aii-1] += 1

print(s.count(0))


    