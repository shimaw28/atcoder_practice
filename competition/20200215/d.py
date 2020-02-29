N, K = map(int, input().split())
A = [int(i) for i in input().split()]

import itertools
import heapq

l = []
heapq.heapify(l)

for ai in itertools.combinations(A, 2):
    heapq.heappush(l, ai[0]*ai[1])

for ki in range(K):
    ans = heapq.heappop(l)

print(ans)