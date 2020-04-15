# https://atcoder.jp/contests/abc138/tasks/abc138_d
#　木探索

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

from collections import deque

N, Q = MAP()
counter = [0]*N
tree = [[] for _ in range(N)]
parent = [-1]*N
for _ in range(N-1):
    a, b = MAP()
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

for _ in range(Q):
    p, x = MAP()
    counter[p-1] += x

q = deque()
q.append(0)

while q:
    index = q.pop()
    pindex = parent[index]
    for i in tree[index]:
        if i == pindex:
            continue
        counter[i] += counter[index]
        parent[i] = index
        q.append(i)

print(*counter)



