def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()
h = LIST()

INF = 10**23

dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    for j in range(1, K+1):
        if i - j < 0:
            continue
        dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

print(dp[-1])