A = []
for _ in range(3):
    A.append([int(i) for i in input().split()])

N = int(input())

grid = [[0] * 3] + [[0] * 3] + [[0] * 3]

for i in range(N):
    b = int(input())

    for j in range(3):
        for k in range(3):
            if b == A[j][k]:
                grid[j][k] = 1

ans = "No"

for j in range(3):
    if sum(grid[j]) == 3:
        ans = "Yes"


for k in range(3):
    tmp = 0
    for j in range(3):
        tmp += grid[j][k]
    if tmp == 3:
        ans = "Yes"

tmp = 0
for i in range(3):
    tmp += grid[i][i]
if tmp == 3:
    ans = "Yes"

tmp = 0
for i in range(3):
    tmp += grid[i][2-i]
if tmp == 3:
    ans = "Yes"


print(ans)
