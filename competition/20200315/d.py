def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()

import itertools
import collections

alphabet = 'abcdefghijklmnopqrstuvwxyz'

a_set = set()
for w in itertools.product(range(N), repeat=N):
    # print(w, end=", ")
    seen = {}

    i = 0
    for l in w:
        if l not in seen.keys():
            seen[l] = i
            i += 1

    # print(seen, end="")

    ans = [0] * N

    for i in range(len(ans)):
        ans[i] = seen[w[i]]

    if tuple(ans) not in a_set:
        print("".join([alphabet[i] for i in ans]))
        a_set.add(tuple(ans))




