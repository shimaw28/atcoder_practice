# https://atcoder.jp/contests/arc043/tasks/arc043_a

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, A, B = MAP()
S = []
for _ in range(N):
    S.append(INT())

if max(S) - min(S) == 0:
    print(-1)
else:
    P = B / (max(S) - min(S))
    Q = A - P * (sum(S)/N)

    print(P, Q)
