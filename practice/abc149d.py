# https://atcoder.jp/contests/abc149/tasks/abc149_d

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()
R, S, P = MAP()
T = input()

point = {"r": P, "s": R, "p": S}


wins = [0] * N
ans = 0
for i in range(N):
    if i < K:
        ans += point[T[i]]
        wins[i] = 1
        continue
    if T[i] == T[i-K] and wins[i-K] == 1:
        continue
    else:
        ans += point[T[i]]
        wins[i] = 1

print(ans)        