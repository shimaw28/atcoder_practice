# atcoder https://atcoder.jp/contests/dp/tasks/dp_d
def main():
    N, W = map(int, input().split())
    w, v = [], []
    for _ in range(N):
        wi, vi = map(int, input().split())
        w.append(wi)
        v.append(vi)


    dp = [[0 for j in range(W+1)] for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][W])

main()