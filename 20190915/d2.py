import numpy as np

n, m = map(int, input().split())
a = np.array([int(i) for i in input().split()])

for _ in range(m):
    imax = np.argmax(a)
    a[imax] = a[imax] // 2

print(a.sum())

