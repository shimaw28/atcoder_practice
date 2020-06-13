S = input()

res = [0] * 2019
res[0] = 1

d = 1
a = 0

for c in reversed(S):
    a += int(c) * d
    a %= 2019
    res[a] += 1
    d *= 10
    d %= 2019

ans = 0
for r in res:
    ans += r*(r-1) // 2
print(ans)