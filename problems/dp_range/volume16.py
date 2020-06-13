# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
# Daruma Otoshi

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
w = LIST()


dp = [[0]*n for _ in range(n+1)]

def check(left, length):
    ret = dp[length-1][left]
    for k in range(length-1, )