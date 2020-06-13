# Longest Common Subsequence ploblem
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja

q = int(input())


for _ in range(q):
    X = input()
    Y = input()

    dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print(dp[-1][-1])


