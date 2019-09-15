n, m = map(int, input().split())
a = [int(i) for i in input().split()]

a.sort(reverse=True)

for _ in range(m):
    a[0] = a[0] // 2

    #swap
    rank = 0
    a0 = a[0]
    for i in range(1, n):
        if a[i] <= a0:
            break
        else:
            a[i-1] = a[i]
            a[i] = a0

print(sum(a))
