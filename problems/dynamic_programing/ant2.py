#p56
# longest common subsequence

n, m = 4, 4
a = "abcd"
b = "becd"

dp = [[0 for j in range(m+1)] for i in range(n+1)]

a = "0" + a
b = "0" + b

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n][m])