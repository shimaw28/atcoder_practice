def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
A = LIST()

ans = 0
b = {}
for i in range(N):
    l = A[i] + (i+1)
    r = (i+1) - A[i]
    if r in b:
        ans += b[r]
    if l in b:
        b[l] += 1
    else:
        b[l] = 1

print(ans)