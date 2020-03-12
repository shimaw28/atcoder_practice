# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

R, C = MAP()
M = []
for _ in range(R):
    M.append(LIST())

ans = 0
for i in range(2 ** R):
    tmp = 0
    for j in range(C):
        tmp2 = 0
        for k in range(R):
            if i >> k & 1:
                tmp2 += (M[k][j]+1) % 2
            else:
                tmp2 += (M[k][j])
        tmp += max(tmp2, R-tmp2)
    ans = max(ans, tmp)
print(ans)
