def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
A = LIST()

ans = 1
for i in range(N):
    if A[i] == 0:
        print(0)
        exit()

for i in range(N):
    ans *= A[i]
    if ans > 10**18:
        ans = -1
        break
print(ans)