import math
import itertools

N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

def get_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

ans = 0
n = 0
for p in itertools.permutations(xy, N):
    d = 0
    for i in range(len(p)-1):
        d += get_dist(p[i], p[i+1])
    ans += d
    n += 1

print(ans / n)
