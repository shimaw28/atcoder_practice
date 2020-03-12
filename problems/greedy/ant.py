#p42 コイン問題
values = [1, 5, 10, 50, 100, 500]
coins = [3, 2, 1, 3, 0, 2]
a = 620

ans = 0
for i in range(5, -1, -1):
    t = min(a//values[i], coins[i])
    a -= t*values[i]
    ans += t

print(ans)