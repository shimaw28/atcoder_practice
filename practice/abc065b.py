# https://atcoder.jp/contests/abc065/tasks/abc065_b

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
a = []
for _ in range(N):
    a.append(INT() - 1)

light_idx = 0

ans = 0
while True:
    light_idx = a[light_idx]
    ans += 1

    if light_idx == 1:
        break

    if ans > N:
        ans = -1
        break

print(ans)
