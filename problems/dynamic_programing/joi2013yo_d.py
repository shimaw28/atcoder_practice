# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

D, N = MAP()
T = []
for _ in range(D):
    T.append(INT())
A, B, C = [], [], []
for _ in range(N):
    a, b, c = MAP()
    A.append(a); B.append(b); C.append(c)

DP = [[None] * D for _ in range(N)]

for i in range(N):
    if A[i] <= T[0] <= B[i]:
        DP[i][0] = 0


for i in range(1, D):
    for j in range(N):
        if A[j] <= T[i] <= B[j]:
            DP[j][i] = 0
            for k in range(N):  
                if DP[k][i-1] != None:
                    DP[j][i] = max(DP[j][i], DP[k][i-1] + abs(C[k] - C[j]))

ans = 0
for i in range(N):
    if DP[i][-1] != None:
        ans = max(ans, DP[i][-1])
print(ans)