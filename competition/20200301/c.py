N, M = map(int, input().split())

ans = 0
num = [None] * N

for _ in range(M):
    s, c = map(int, input().split())

    if s == 1 and c == 0:
        ans = -1
        break

    if num[s-1] is None:
        num[s-1] = c
    elif num[s-1] == c:
        pass
    else:
        ans = -1
        break

if num[0] is None:
    if M == 0:
        if N == 1:
            ans = 0
        else:
            num[0] = 1
    else:
        num[0] = 1

if ans == -1:
    pass
else:
    for i in range(N):
        if num[i] is None:
            num[i] = 0
        ans += 10**(N-i-1) * num[i]

ans2 = ans
n = 0
while ans2 > 0:
    ans2 // 10
    
print(ans)

        