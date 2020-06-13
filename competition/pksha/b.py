import copy
import bisect # use bisect so the whole can be calculated in O(NlogN)

def solution(A, K):
    if len(A) - K == 1:
        return min(A[0], A[-1])
    
    a = copy.deepcopy(A[K:])
    a.sort()
    
    ans = a[-1] - a[0] #max - min

    for i in range(len(A)-K):
        left_idx = bisect.bisect_left(a, A[i])
        a.insert(left_idx, A[i])

        right_idx = bisect.bisect_left(a, A[i+K])
        a.pop(right_idx)

        ans = min(ans, a[-1] - a[0])

    return ans







A = [5, 3, 6, 1, 3]
K = 2

print(solution(A, K))