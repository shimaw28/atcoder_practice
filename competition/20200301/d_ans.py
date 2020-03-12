from collections import deque
n, m, k = map(int, input().split())
a = [list(map(lambda x: int(x)-1, input().split())) for i in range(m)]
c = [list(map(lambda x: int(x)-1, input().split())) for i in range(k)]

mp = [set() for _ in range(n)]
bl = [set() for _ in range(n)]

for af, bf in a:
    mp[af].add(bf)
    mp[bf].add(af)
for cf, df in c:
    bl[cf].add(df)
    bl[df].add(cf)

sz=[0]*n
for i in range(n):
    if sz[i] > 0:
        continue

    d = deque()
    reach = {i}
    d.append(i)
    while d:
        s = d.pop()
        for g in mp[s]:
            if g in reach:
                continue
            else:
                reach.add(g)
                d.append(g)
    
    for j in reach:
        sz[j] = len(reach)
    
    for k in reach:
        for j in bl[k]:
            if j in reach:
                sz[k] -= 1

for i in range(n):
    sz[i] -= len(mp[i])+1

print(*sz)