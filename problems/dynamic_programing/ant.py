#p52 napsack

n = 4
WN = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5

Wlist, Vlist = [], []

for wni in WN:
    Wlist.append(wni[0]); Vlist.append(wni[1])

dp = [[0 for j in range(W+1)] for i in range(n+1)] #dptable

# dp[i][j]: i版目以降の品物の重さの総額がj以下となるように選んだ時の、価値の総和の最大値
# dp[n][j]=0
# dp[i][j]= {dp[i+1][j]  (j<w[i]),
#            dp[i+1][j-w[i]]+v[i] (それ以外)}

for i in range(n-1, -1, -1):
    for j in range(W+1):
        if j < Wlist[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j-Wlist[i]]+Vlist[i], dp[i+1][j])

print(dp[0][W])

# もしくは
# dp[i][j]: i版目までの品物の重さの総額がj以下となるように選んだ時の、価値の総和の最大値
# dp[0][j]=0
# dp[i][j]= {dp[i−1][j]  (j<w[i]),
#            dp[i−1][j-w[i]]+v[i] (それ以外)}

dp = [[0 for j in range(W+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(W+1):
        if j < Wlist[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-Wlist[i-1]]+Vlist[i-1], dp[i-1][j])

print(dp[n][W])

# 個数制限なし
n = 3
w = [3, 4, 2]
v = [4, 5, 3]
W = 7

dp = [[0 for j in range(W+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(W+1):
        if j < w[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w[i-1]]+v[i-1])

print(dp[n][W])

# Wが大きい場合、価値に対する最小のwを求める。

n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5
INF = 100

dp = [[None for j in range(max(v)*n + 1)] for i in range(n+1)]

for i in range(max(v)*n):
    dp[0][i] = INF
dp[0][0] = 0

for i in range(n):
    for j in range(max(v)*n):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])

res = 0
for i in range(max(v)*n):
    if dp[n][i] <= W:
        res = i
print(dp[n][max(v)+n])