# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d

N = int(input())
num = list(map(int, input().split()))
n = num[-1]
DP = [[0 for _ in range(21)] for _ in range(N+1)]
DP[1][num[0]] = 1

for i in range(N):
    for j in range(21):
        if(j - num[i] >= 0):
            DP[i+1][j] += DP[i][j-num[i]]
        if(j + num[i] <= 20):
            DP[i+1][j] += DP[i][j+num[i]]
print(DP[N-1][num[-1]])

        
