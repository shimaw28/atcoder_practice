#atcoder https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = [int(i) for i in input().split()]

INF = 10**4

dp = [INF for i in range(N)]

dp[0] = 0
dp[1] = abs(h[0]-h[1])

for i in range(2, N):

    dp[i] = min(
        dp[i-2]+abs(h[i-2]-h[i]),
        dp[i-1]+abs(h[i-1]-h[i])
        )


print(dp[N-1])

