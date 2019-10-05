l = int(input())
a = []
for _ in range(l):
    a.append(int(input()))
#%%
import numpy as np

#%%
# l, a = 4, [1, 0, 2, 3]

#%%
a = np.array(a)
a_max = max(a)
ear = np.zeros((1,l), dtype=int)
#%%



#%%
def sunuke(a, start, smallest_ringo):
    if max(abs(a)) >= a_max:
        return smallest_ringo
    #going right
    for i in range(start + 1, l):
        new_a = a.copy()
        new_a[start:i] -= 1
        new_ringo = sum(abs(new_a))
        if smallest_ringo > new_ringo:
            smallest_ringo = new_ringo
            new_start = i

    #going left
    for i in range(start):
        new_a = a.copy()
        new_a[i:start] -= 1
        if smallest_ringo > new_ringo:
            smallest_ringo = new_ringo
            new_start = i

    return sunuke(new_a, new_start, smallest_ringo)

#%%
smallest_ringo = sum(abs(a)
for i in range(l):
    smallest_ringo = min(smallest_ringo, sunuke(a, i, smallest_ringo))

print(smallest_ringo)
#%%
