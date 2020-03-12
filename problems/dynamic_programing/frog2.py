#atcoder https://atcoder.jp/contests/dp/tasks/dp_b

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))


    dp = [0] * N
    dp[0] = 0

    for i in range(1, N):

        dp[i] = min(
            dp[k] + abs(h[i]-h[k]) for k in range(max(i-K,0), i)
        )

    print(dp[N-1])

main()