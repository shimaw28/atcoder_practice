# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3184906#1
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = int(input())
R, C = [0]*N, [0]*N

for i in range(N):
    R[i], C[i] = MAP()

dp = [[float("INF")]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

# arr_shape = [[0, 0] * N for _ in range(N)]
# for i in range(N):
#     arr_shape[i][i] = [R[i], C[i]]


for i in range(1, N+1):
    for l in range(N-1):
        r = l+i
        if r <= l or N-1 < r:
            continue
        a = R[l]
        c = C[r]
        dp[l][r] = min(
            dp[l][r-1] + a*R[r]*c,
            dp[l+1][r] + a*C[l]*c
        )
        print(R[l], C[l], R[l+1], C[r], "and", R[l], C[r-1], R[r], C[r])
        

print(dp[0][-1])