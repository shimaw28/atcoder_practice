n, k = map(int, input().split())
h = [int(hi) for hi in input().split()]

ans = 0
for hi in h:
    if hi >= k:
        ans += 1

print(ans)