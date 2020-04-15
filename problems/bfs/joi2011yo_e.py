# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

H, W, N = MAP()
m = []
check = {}
for i in range(H):
    mi = list(input())
    for j, mii in enumerate(mi):
        if mii == "X" or mii == ".":
            continue
        check[mii] = [i, j]
    m.append(mi)

check["0"] = check["S"]

from collections import deque

ans = 0
for i in range(1, N+1):
    sx, sy = check[str(i-1)]
    gx, gy = check[str(i)]
    que = deque()
    que.append((sx, sy))
    fp = [[-1]*W for _ in range(H)]
    fp[sx][sy] = 0

    while que:
        x, y = que.popleft()
        if x==gx and y==gy:
            ans += fp[x][y]
            break

        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for di in range(4):
            nx, ny = x+dx[di], y+dy[di]
            if -1 < nx < H and -1 < ny < W \
                and m[nx][ny] != "X" and fp[nx][ny] == -1:
                
                fp[nx][ny] = fp[x][y] + 1
                que.append((nx, ny))

print(ans)