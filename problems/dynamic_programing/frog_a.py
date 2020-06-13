def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
h = LIST()

INF = 10**23
dp = [INF] * N

dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(abs(h[i] - h[i-1]) + dp[i-1],
                abs(h[i]- h[i-2]) + dp[i-2])

print(dp[-1])