# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
N = int(input())
A, B, d = [], [], []
for _ in range(N):
    a, b = map(int, input().split())
    di = b - a
    A.append(a); B.append(b)
    d.append(di)

A.sort()
B.sort()

start = A[N//2]
end = B[N//2]

ans = sum(d)


for i in range(N):
    ans += abs(A[i] - start) + abs(B[i] - end)

print(ans)