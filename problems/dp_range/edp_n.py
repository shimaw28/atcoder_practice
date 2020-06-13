# https://atcoder.jp/contests/dp/tasks/dp_n
# slimes
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
a = LIST()

S = [0]
for i in range(N):
    S.append(S[i-1] + a[i])

DP = [[None for r in range(N+1)] for l in range(N)]

def dp(l, r):
    if r <= l+1:
        return 0
    if DP[l][r] != None:
        return DP[l][r]
    DP[l][r] = S[r]-S[l]+min([dp(l, i) + dp(i, r) for i in range(l+1, r)])
    return DP[l][r]

print(dp(0, N))
