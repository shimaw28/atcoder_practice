n, k = map(int, input().split())
a = list(map(int, input().split()))

# print(n, k, a)

#%%

# n, k, a = 3, 7, [1, 6, 3]


#%%
import math


#%%
format(7, "b").zfill(10)

#%%
digit = int(math.log2(k)) + 1

#%%

bi_list = [[]]*digit
for ai in a:
    bi = format(ai, "b").zfill(digit)
    for i in range(digit):
        print(int(bi[i]))
        bi_list[i].append(int(bi[i]))
        print(bi_list)
#%%
bi_list

#%%
[[]]*3

#%%
