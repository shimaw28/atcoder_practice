n = int(input())
alist = []
for _ in range(5):
    alist.append(int(input()))


#%%
# n, alist = 5, [3, 2, 4, 3, 5]


#%%
if n <= min(alist):
    print(5)
else:
    print((n-1)//min(alist)+5)