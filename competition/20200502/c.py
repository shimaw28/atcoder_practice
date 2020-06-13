def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import itertools

N, M, Q = MAP()
a, b, c, d = [], [], [], []
for _ in range(Q):
    ai, bi, ci, di = MAP()
    a.append(ai-1); b.append(bi-1); c.append(ci); d.append(di)


def solve(lst):
    ans = 0
    for i in range(Q):
        if lst[b[i]] - lst[a[i]] == c[i]:
            ans += d[i]
    return ans

ans = 0
for A in itertools.combinations_with_replacement(range(1, M+1), N):
    ans = max(ans, solve(A))

print(ans)