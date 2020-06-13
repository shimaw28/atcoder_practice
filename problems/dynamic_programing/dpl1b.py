# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja
#　ナップザック # knapsack

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, W = MAP()

vw = []
for _ in range(N):
    vw.append(list(MAP()))

dp = [0]*(W+1)
for w in range(1, W+1):
    for i in range(N):
        vi = vw[i][0]
        wi = vw[i][1]
        if w - wi >= 0:
            dp[w] = max(dp[w], dp[w-wi]+vi)

print(dp[W])


