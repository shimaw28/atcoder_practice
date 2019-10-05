n, m, k = map(int, input().split())
b = list(map(int, input().split()))

#%%
# n, m, k = 4, 100, 2
# b = [20, 30, 75, 80]


#%%
b_dif = []
for i in range(len(b)-1):
    b_dif.append(b[i+1] - b[i])

b_dif.sort()
#%%
if k == 1:
    print(sum(b_dif) + k)
else:
    print(sum(b_dif[:-(k-1)]) + k)


#%%
