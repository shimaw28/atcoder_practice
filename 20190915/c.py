n, k, q = map(int, input().split())
a = []
for _ in range(q):
    a.append(int(input()))

# print(n,k,q, a)

points = {i:0 for i in range(n)}

# print(points)
for ai in a:
    points[ai-1] += 1

for i in range(n):
    if k - q + points[i] > 0:
        print("Yes")
    else:
        print("No")