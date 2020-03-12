# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
INF = 1000000
m = int(input())
a = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
b = [tuple(map(int, input().split())) for _ in range(n)]

bs = set(b)

a.sort()
b.sort()

for bi in b:
    dx = bi[0] - a[0][0]
    dy = bi[1] - a[0][1]

    for ai in a[1:]:
        if (ai[0]+dx, ai[1]+dy) in bs:
            continue
        break
    else:
        break

print(dx, dy)