# https://atcoder.jp/contests/dp/tasks/dp_e
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, W = MAP()
w, v = [], []

for _ in range(N):
    wi, vi = MAP()
    w.append(wi)
    v.append(vi)
max_v = N*max(v)
DP = [[float("INF")] * (N+1) for _ in range(max_v+1)]
DP[0][0] = 0

for i in range(1, max_v+1):
    for j in range(N):
        if v[j-1] > i:
            DP[i][j+1] = DP[i][j]
        else:
            DP[i][j+1] = min(
                DP[i][j],
                DP[i-v[j-1]][j] + w[j]
            )

ans = 0
for i in range(1, max_v+1):
    if DP[i][N] <= W:
        ans = i

print(ans)