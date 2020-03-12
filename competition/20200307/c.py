def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

A, B = MAP()

ans = -1
for i in range(1, 1250):
    if int(i * 0.08) == A and int(i*0.1) == B:
        ans = i
        break

print(ans)