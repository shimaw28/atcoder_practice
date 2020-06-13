# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
# まずmapの周りに空スペースを儲け、bfsで判定。建物があったら壁を数える。

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

W, H = MAP()
m = []
for _ in range(H):
    m.append([0]+LIST()+[0])

m = [[0]*(W+2)] + m + [[0]*(W+2)]
fp = [[-1]*(W+2) for _ in range(H+2)]

from collections import deque
que = deque()
que.append((0, 0))
fp[0][0] = 0

ans = 0
while que:
    x, y = que.popleft()
    # ans += cnt_margin(x, y)

    if x % 2 == 0:
        dx = [0, 0, -1, -1, 1, 1]
        dy = [1, -1, -1, 0, -1, 0]
    else:
        dx = [0, 0, -1, -1, 1, 1]
        dy = [1, -1, 0, 1, 0, 1]

    for i in range(6):
        nx, ny = x+dx[i], y+dy[i]
        if -1 < nx < H+2 and -1 < ny < W+2:
            if m[nx][ny] == 1: #空き地から見て隣に建物があったら
                ans += 1 #壁としてカウント
            elif fp[nx][ny] == -1:
                que.append((nx, ny))
                fp[nx][ny] = 0

print(ans)
