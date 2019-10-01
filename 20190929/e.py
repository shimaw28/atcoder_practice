n, m = map(int, input().split())

MAX = 100000000
dp = [MAX for _ in range(1 << n)]
dp[0] = 0


for i in range(m):
    a, b = map(int, input().split())
    c = map(int, input().split())
    si = 0

    for cc in c:
        si += 1 << (cc-1)
    for s in range(1 << n):
        sn = s | si
        dp[sn] = min(dp[sn], dp[s]+a)

if dp[-1] == MAX:
    print(-1)
else:
    print(dp[-1])