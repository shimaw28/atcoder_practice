# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
# パ研軍旗
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
S = []
for _ in range(5):
    S.append(input())

colors = ["R", "B", "W"]
DP = [[float("INF")] * N for _ in range(3)] #R, B, W

def count_color(column, color):
    cnt = 0
    for j in range(5):
        if S[j][column] != colors[color]:
            cnt += 1
    return cnt

for c in range(3):
    DP[c][0] = count_color(0, c)


for column in range(1, N):
    for c in range(3):
        DP[c][column] = min(
            DP[(c+1)%3][column-1] + count_color(column, c),
            DP[(c+2)%3][column-1] + count_color(column, c)
        )

ans = float("INF")                
for c in range(3):
    ans = min(ans, DP[c][-1])
print(ans)        