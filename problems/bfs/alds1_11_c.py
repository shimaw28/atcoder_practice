# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()

U, K, V = [], [], []
parents = [] * n

for _ in range(n):
    u, k, *v = MAP()
    U.append(u-1)
    K.append(k)
    vi = [i-1 for i in v]
    V.append(vi)

steps = [-1] * n

from collections import deque

que = deque()
que.append(0)
steps[0] = 0

while que:
    node = que.popleft()
    for vi in V[node]:
        que.append(vi)
        if steps[vi] == -1:
            steps[vi] = steps[node] + 1
        else:
            steps[vi] = min(steps[node] + 1, steps[vi])

for i, s in enumerate(steps):
    print(i+1, s)