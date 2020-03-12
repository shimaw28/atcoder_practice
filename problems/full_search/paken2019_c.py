# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c


N, M = map(int, input().split())
A = []
for _ in range(N):
    ai = [int(i) for i in input().split()]
    A.append(ai)

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        point = 0
        for k in range(N):
            point += max(A[k][i], A[k][j])
        ans = max(ans, point)


print(ans)
