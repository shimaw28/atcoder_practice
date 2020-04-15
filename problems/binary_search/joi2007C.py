# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


N, M = MAP()
P = []
for _ in range(N):
    P.append(INT())

p12 = set()
for p1 in P + [0]:
    for p2 in P + [0]:
        p12.add(p1 + p2)
p12 = list(p12)
p12.sort()

p34 = p12.copy()
# p34 = []
# for p3 in P + [0]:
#     for p4 in P + [0]:
#         p34.append(p3 + p4)
# p34.sort()

# ans = 0
# for p in p12:
#     left, right = 0, len(p34)-1
#     if p + p34[left] > M:
#         continue
#     while right - left > 1:
#         mid = (left + right) // 2
#         if p + p34[mid] <= M:
#             left = mid
#         else:
#             right = mid
#     ans = max(ans, p + p34[left])
# print(ans)

import bisect
ans = 0
for i in range(len(p12)):
    if p12[i] > M:
        break
    q = s[bisect.bisect_left(p34, M-p12[i])-1]
    ans = max(p12[i]+q)
print(ans)    