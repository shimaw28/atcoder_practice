#p38

n, m = 10, 10
maze = [
    "#S######.#",
    "......#..#",
    ".#.##.##.#",
    ".#........",
    "##.##.####",
    "....#....#",
    ".#######.#",
    "....#.....",
    ".####.####",
    "....#...G#"
]

INF = 10**9
#スタート地点とゴール地点
sx, sy = 0, 1
gx, gy = 9, 8

#上下左右の移動を表す
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

#スタートからの最短距離（初期化)
from collections import deque
d = [[INF for i in range(n)] for j in range(m)]
#Queueを作成
queue = deque()

#スタート地点を
queue.append((sx, sy))
d[sx][sy] = 0

while len(queue) > 0:
    p = queue.popleft()
    x, y, = p[0], p[1]

    if x==gx and y==gy:
        break

    #移動
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i] #新しいますをnx,nyとする

        #枠内かつINFであればdを記入する
        if 0<=nx and nx<n and \
                0<=ny and ny<m and \
                maze[nx][ny] != "#" and d[nx][ny] == INF:
            d[nx][ny] = d[x][y]+1
            queue.append((nx, ny))

print(d[gx][gy])
