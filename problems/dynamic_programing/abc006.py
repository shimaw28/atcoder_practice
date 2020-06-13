# https://atcoder.jp/contests/abc006/tasks/abc006_4
# トランプソート
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
c = []
for _ in range(N):
    c.append(INT())

DP = [float("INF")] * N
DP[0] = c[0]

for i in range(1, N):
    l = 0
    r = N-1
    while r - l > 1:
        mid = (l+r) // 2
        if DP[mid] > c[i]:
            r = mid
        else:
            l = mid
    if DP[r-1] >= c[i]:
        DP[r-1] = c[i]
    else:
        DP[r] = c[i]

print(DP.count(float("INF")))