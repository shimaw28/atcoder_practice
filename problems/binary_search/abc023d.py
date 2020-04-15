def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


N = INT()
H, S = [], []
for _ in range(N):
    h, s = MAP()
    H.append(h)
    S.append(s)


def judge(lim):
    lst = []
    for i in range(N):
        lst.append((lim - H[i])//S[i])
    lst.sort()
    for j in range(N):
        if lst[j] < j:
            return False
    return True

ok, ng = 10**20, -1

while ok - ng > 1:
    mid = (ng + ok) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)
    
