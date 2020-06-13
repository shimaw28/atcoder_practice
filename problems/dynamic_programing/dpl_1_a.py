# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, m = MAP()
c = LIST()

price = [float("INF")] * (n+1)
price[0] = 0

for i in range(n+1):
    for j in range(m):
        if i - c[j] < 0:
            continue
        price[i] = min(price[i], price[i-c[j]] + 1)

print(price[-1])

