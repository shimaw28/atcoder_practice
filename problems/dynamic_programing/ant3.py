# 個数制限つき部分和

n = 3
a = [3, 5, 8]
m = [3, 2, 2]
K = 17


# dp[i+1][j]:= i番目まででjが作れるか
dp = [[False for j in range(K+1)] for i in range(n+1)]

for i in range(len(dp)):
    dp[i][0] = True


for i in range(n):
    for j in range(K+1):
        for k in range(m[i]+1):
            if j>=k*a[i]:
                dp[i+1][j] = (dp[i][j] or dp[i+1][j] or dp[i][j-k*a[i]])

if dp[n][K]:
    print("Yes")
else:
    print("No")


# より効率的な解法
# あまりの数を考える

dp = [-1 for i in range(K+1)]
dp[0] = 0

for i in range(n):
    for j in range(K+1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j - a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j-a[i]]-1

if dp[K] >= 0:
    print("Yes")
else:
    print("No")