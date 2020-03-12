#　p63　最長増加部分数列問題
n = 5
a = [4, 2, 3, 1, 5]

# dp[i]: 最後がaiであるような最長の増加部分列の長さ
dp = [0 for i in range(n)]

res = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)
    res = max(res, dp[i])

print(res)


