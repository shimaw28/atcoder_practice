import itertools
import numpy as np
import math
n = int(input())

x = []
for i in range(n):
    x.append(int(input()))

xa = np.zeros((math.factorial(n),n)).astype(int)

xa.shape
for i, l in enumerate(itertools.permutations(x)):
    xa[i,:] = l

max_diff = np.abs(xa[:, 1:] - xa[:, :-1]).sum(axis=1).max()
print(max_diff)
