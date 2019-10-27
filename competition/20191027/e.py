N, K = map(int, input().split())
A = [int(i) for i in input().split()]
F = [int(i) for i in input().split()]

A.sort(reverse=True)
F.sort(reverse=True)

i = 0
while K != 0:
    if sum(A) == 0:
        break
    if A[i] == 0:
        i += 1
        continue
    A[i] -= 1
    K -= 1


A.sort()

ans = 0
for i in range(N):
    ans = max(ans, A[i] * F[i])
print(A, F)
print(ans)