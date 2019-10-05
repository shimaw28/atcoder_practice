import math
n, p = map(int, input().split())


if n == 1:
    print(p)
    exit()

ans = 1
for i in range(2, p+1):
    power = i**n
    if p % power == 0:
        ans = i
    if power >= p:
        break
print(ans)