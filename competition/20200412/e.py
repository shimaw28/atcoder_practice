def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()

mod = 10**9+7

cnt = [0]*K


for i in reversed(range(1, K+1)):
    a = pow(K//i, N, mod)
    cnt[i-1] = a

    b = 2
    while b*i <= K:
        cnt[i-1] -= cnt[b*i-1]
        b += 1

ans = 0
for i in range(K):
    ans += (i+1)*cnt[i] % mod

print(ans % mod)