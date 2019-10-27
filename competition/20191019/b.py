N = int(input())
d = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        ans += d[i] * d[j]

print(ans)