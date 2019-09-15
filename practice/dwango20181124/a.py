n = int(input())
a = [int(a) for a in input().split()]




#%%
ave = sum(a)/len(a)

least_dif = 99999
ans = 0
for i, num in enumerate(a):
    dif = abs(num - ave)
    if dif < least_dif:
        least_dif = dif
        ans = i

print(ans)
#%%
idx_a = []
idx_b = []
idx_c = []


#%%
