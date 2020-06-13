# atcoder https://atcoder.jp/contests/dp/tasks/dp_c

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()

DP = [[0] * 3 for _ in range(N)]


for i in range(N):
    abc = LIST()
    if i == 0:
        DP[0] = abc
        continue
    for j in range(3):
        DP[i][j] = max(DP[i-1][(j+1)%3] + abc[j],
                       DP[i-1][(j+2)%3] + abc[j])


print(max(DP[-1]))