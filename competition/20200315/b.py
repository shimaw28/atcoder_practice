def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

H, W = MAP()

ans = 0
if H == 1 or W == 1:
    ans = 1
elif W % 2 == 0:
    ans = (W//2) * H
else:
    if H % 2 == 0:
        ans = ((W+1)//2 * (H//2)) + (((W+1)//2-1) * (H//2))
    else:
        ans = ((W+1)//2 * ((H+1)//2)) + (((W+1)//2-1) * (H//2))


print(ans)