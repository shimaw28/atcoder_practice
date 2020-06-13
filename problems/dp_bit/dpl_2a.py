# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3367415#1


def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

V, E = MAP()
G = []
for _ in range(E):
    s, t, d = MAP()
    G.append(((s, t), d))

DP = [[-1] * V for _ in range(1<<V)]
dist = [[float("INF")] * V for _ in range(V)]

for i in range(E):
    s, t = G[i][0]
    d = G[i][1]
    dist[s][t] = d


def tsp(s, v, dp, n):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1<<n)-1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float("INF")
    for u in range(n):
        if (s>>u & 1) == 0:
            res = min(
                res,
                tsp(s|(1<<u), u, dp, n) + dist[v][u]
            )
    dp[s][v] = res
    return res

ans = tsp(0, 0, DP, V)
print(ans if ans != float("INF") else -1)

