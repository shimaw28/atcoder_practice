#https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

d = INT()
n = INT()
m = INT()
d = [0]
for _ in range(n-1):
    d.append(int(input()))
k = []
for _ in range(m):
    k.append(int(input()))

d.sort()
k.sort()

ans = 0
for ki in k:
    