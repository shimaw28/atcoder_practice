def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 998244353


N = INT()
XD = []
for _ in range(N):
    xi, di = MAP()
    XD.append((xi, di))

XD.sort(reverse=True)

lst = [0] * N
ans = 2 ** N
for i in range(1, N):
    xi, di = XD[i][0], XD[i][1]

    include = []
    for j in range(1, j+1):
        if XD[i-j] < (xi + di):
            include.append(i-j)
            lst[i] += 1
        else:
            break

    for inc in include:
        ans -= 1
        ans -= lst[inc]
    ans -= 

    
print(ans % MOD)