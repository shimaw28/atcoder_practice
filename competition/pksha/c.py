from collections import Counter


def solution(A):
    if A.count(0) >= 10**9:
        return -1

    S = [0] #cumsum
    for a in A:
        S.append(S[-1] + a)
    
    cnt = Counter(S) #count the same pair of cumsum

    ans = 0

    for v in cnt.values():
        ans += v * (v-1) // 2   #Comb(n, 2)
        if ans >= 10**9:
            return -1

    return ans

A = [0]
print(solution(A))