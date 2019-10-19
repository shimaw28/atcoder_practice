# p73 POJ2431
# ガソリン
import heapq
from collections import deque

N = 4
L = 25
P = 10
A = [10, 14, 20, 21]
B = [10, 5, 2, 4]

A = deque(A)
B = deque([-bi for bi in B])
queue = []

ans = 0
for x in range(1, L):
    P -= 1

    if len(A)>0 and x == A[0]:
        A.popleft()
        b = B.popleft()
        heapq.heappush(queue, b)
    
    if P == 0:
        if len(queue) == 0:
            ans = -1
            break

        p = -1 * heapq.heappop(queue) #heappopは最小値を取り出すので
        P += p
        ans += 1

print(ans)