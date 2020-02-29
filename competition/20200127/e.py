

H, N = map(int, input().split())
A, B = [], []
for _ in range(N):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)

inf = 10**23

d = [inf] * (H+1)
d[0] = 0
for i in range(1, H+1):
    for abi in range(N):
        if A[abi] >= i:
            d[i] = min(d[i], B[abi])
        else:
            d[i] = min(d[i], d[i-A[abi]] + B[abi])


print(d[H])


