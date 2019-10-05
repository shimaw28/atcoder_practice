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
sx, sy = 1, 0
gx, gy = 8, 9

#上下左右の移動を表す
dx, dy = [-1, 0, 1, 0], [0, -1, 1, 0]

#スタートからの最短距離（初期化)
from collections import deque
d = [[INF]*n]*m
#Queueを作成
queue = deque()

#スタート地点を
queue.append((sy, sx))
d[sy][sx] = 0

while len(queue) > 0:
    p = queue.popleft()
    y, x, = p[0], p[1]

    if x==gx and y==gy:
        break

    #移動
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i] #新しいますをnx,nyとする

        #枠内かつINFであればdを記入する
        if 0<=nx and nx<n and \
                0<ny and ny<m and \
                maze[ny][nx] != "#" and d[ny][nx] == INF:
            d[ny][nx] == d[y][x]+1
            queue.append((ny, nx))

print(d[y][x])
