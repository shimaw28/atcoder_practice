# https://atcoder.jp/contests/dp/tasks/dp_d

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, W = MAP()
w, v = [], []
for _ in range(N):
    wi, vi = MAP()
    w.append(wi)
    v.append(vi)

DP = [[0] * (N+1) for _ in range(W+1)]

for i in range(1, W+1):
    for j in range(1, N+1):
        if i < w[j-1]:
            DP[i][j] = max(
                DP[i][j-1],
                DP[i-1][j])
        else:
            DP[i][j] = max(
                DP[i][j-1],
                DP[i-w[j-1]][j-1] + v[j-1],
                DP[i-1][j])

print(DP[-1][-1])




