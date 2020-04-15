# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d

import copy
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

m = INT()
n = INT()
f = []
for _ in range(n):
    f.append(LIST())

# def dfs(f, i, j, step, max_step):
#     if -1==i or i==n or -1==j or j==m:
#         return step
#     if f[i][j] == 0:
#         return step
    
#     step += 1
#     f_cp = copy.deepcopy(f)
#     f_cp[i][j] = 0

#     for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         max_step = max(max_step, dfs(f_cp, i+ii, j+jj, step, max_step))

#     return max_step

# max_step = 0
# for i in range(n):
#     for j in range(m):
#         max_step = max(max_step, dfs(f, i, j, 0, max_step))

# print(max_step)

def dfs(x, y, d):
    f[x][y] = 0
    nd = d+1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and f[nx][ny] != 0:
            d = max(dfs(nx, ny, nd), d)
    f[x][y] = 1
    return d

chk = set()
for i in range(n):
    for j in range(m):
        if f[i][j] == 1:
            chk.add(dfs(i, j, 1))
print(max(chk))

