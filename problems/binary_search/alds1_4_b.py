def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
S = LIST()
q = INT()
T = LIST()

S.sort()

ans = 0
for ti in T:
    s = 0
    mid = n // 2
    e = n - 1
    while e - s > 1:
        if S[mid] == ti or S[s] == ti or S[e] == ti:
            ans += 1
            break
        elif ti < S[mid]:
            e = mid
            mid //= 2
        elif S[mid] < ti:
            s = mid
            mid = mid + mid//2

print(ans)
