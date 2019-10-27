N = int(input())
L = [int(i) for i in input().split()]

import bisect
L.sort()
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        idx = bisect.bisect_left(L, L[i]+L[j])
        ans += (idx-(j+1))

print(ans)