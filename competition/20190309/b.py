n, m, c = map(int, input().split())
b = [int(x) for x in input().split()]

ans = 0
for _ in range(n):
    a = ([int(x) for x in input().split()])
    equ = 0
    for i in range(m):
        equ += a[i] * b[i]
    equ += c

    if equ > 0:
        ans += 1


print(ans)
#%%
