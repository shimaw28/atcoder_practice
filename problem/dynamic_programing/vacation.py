# atcoder https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
a, b, c = [], [], []
for _ in range(N):
    ai, bi, ci = map(int, input().split())
    a.append(ai); b.append(bi); c.append(ci)


dp = [[0] * N for _ in range(3)] #dp[h][i]: i日目にhを行った場合の最大幸福度
dp[0][0], dp[1][0], dp[2][0]  = a[0], b[0], c[0]

for i in range(1, N):
    dp[0][i] = a[i] + max(dp[1][i-1], dp[2][i-1])
    dp[1][i] = b[i] + max(dp[0][i-1], dp[2][i-1])
    dp[2][i] = c[i] + max(dp[0][i-1], dp[1][i-1])

print(max(dp[h][N-1] for h in range(3)))