# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
#　島はいくつある？

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

w, h = MAP()
c = []
searched = []
for _ in range(h):
    ci = list(MAP())
    c.append(ci)
    searched.append([-1]*w)
# print(c, searched)

def dfs(hi, wi, island_num):
    global ans, searched
    if wi == w or hi == h or wi == -1 or hi == -1:
        return None

    if c[hi][wi] == 0:
        return None

    if searched[hi][wi] == -1:
        searched[hi][wi] = island_num
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                dfs(hi+i, wi+j, island_num)


a = 0
for hi in range(h):
    for wi in range(w):
        dfs(hi, wi, a)
        a += 1

ans_set = set()
for hi in range(h):
    ans_set = ans_set | set(searched[hi])

print(len(ans_set)-1)