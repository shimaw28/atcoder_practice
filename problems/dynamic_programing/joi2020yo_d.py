# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

MOD = 10000

N, K = MAP()
AB = []

A = [-1] * N
DP = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N+1)]
DP[0][0][0] = 1

for i in range(K):
    x, y = MAP()
    A[x-1] = y-1

for i in range(N):
    for j in range(3):
        for k in range(3):
            source = [0, 1, 2]
            if (A[i] >= 0):
                source = [A[i]]
            for v in source:
                if(i >= 2 and v == j and j==k):
                    continue
                DP[i+1][k][v] += DP[i][j][k]
ans = 0
for d in DP[-1]            :
    ans += sum(d)
print(ans % MOD)



