# https://atcoder.jp/contests/abc007/tasks/abc007_3

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

R, C = MAP()
sy, sx = MAP()
gy, gx = MAP()

sy -= 1; sx -= 1; gy -= 1; gx -= 1

c = []
for _ in range(R):
    c.append(input())

d = []
for _ in range(R):
    d.append([-1]*C)

from collections import deque
que = deque()

d[sy][sx] = 0

que.append((sy, sx))

while que:
    y, x = que.popleft()

    if y == gy and x == gx:
        break

    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if c[ny][nx] == "." and d[ny][nx] == -1:
            que.append((ny, nx))
            d[ny][nx] = d[y][x] + 1
print(d[gy][gx])
