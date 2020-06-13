# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, M = MAP()
D = []
for _ in range(N):
    D.append(INT())
C = []
for _ in range(M):
    C.append(INT())

DP = [[float("INF")] * (N+1) for _ in range(M+1)]

for date in range(M+1):
    DP[date][0] = 0

for date in range(1, M+1):
    for city in range(1, N+1):
        if DP[date - 1][city - 1] == float("INF"):
            continue
        DP[date][city] = min(
            DP[date][city], 
            DP[date-1][city],
            DP[date-1][city-1] + D[city-1] * C[date-1]
        )

print(DP[-1][-1])