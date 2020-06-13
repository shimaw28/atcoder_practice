def solution(N, K):
    ans = 0
    while K > 0 and N > 1:
        if N % 2 == 0:
            N //= 2
            ans += 1
            K -= 1
        else:
            N -= 1
            ans += 1
    ans += N-1
    return ans

N, K = 10, 10

print(solution(N, K))