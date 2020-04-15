def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()

ans = 0

for i in range(1, N+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        ans += i

print(ans)
