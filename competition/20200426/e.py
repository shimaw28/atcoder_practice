def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, M, S = MAP()

U, V, A, B = [], [], [], []
for _ in range(M):
    u, v, a, b = MAP()
    U.append(u-1); V.append(v-1); A.append(a), B.append(b)

C, D = [], []
for _ in range(N):
    c, d = MAP()
    C.append(c); D.append(d)

# print(U, V, A, B, C, D)

