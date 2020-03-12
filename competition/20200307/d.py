def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
from collections import deque

S = input()
Q = int(input())

# Queries = []
# for _ in range(Q):
#     Queries.append(list(input().split()))
    
# for Query in Queries:
#     T = int(Query[0])
#     if T == 1:
#         S = S[::-1]
#     else:
#         F = int(Query[1])
#         C = Query[2]
#         if F == 1:
#             S = C + S
#         else:
#             S = S + C
# print(S)

swap = 1
head = deque()
tail = deque()
for _ in range(Q):
    Query = list(input().split())

    if Query[0] == "1":
        swap *= -1
    
    else:
        F, C = Query[1], Query[2]
        if F == "1":
            if swap == 1:
                head.appendleft(C)
            else:
                tail.append(C)
        else:
            if swap == -1:
                head.appendleft(C)
            else:
                tail.append(C)         


print(("".join(head) + S + "".join(tail))[::swap])

