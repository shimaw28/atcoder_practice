def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

K = INT()
A, B = MAP()

ans = False
i = 1
while i <= B:
    if A <= K*i <= B:
        ans = True
        break
    i += 1 

if ans:
    print("OK")
else:
    print("NG")