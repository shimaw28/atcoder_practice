n, k = map(int, input().split())
a = [int(ai) for ai in input().split()]
b = [int(bi) for bi in input().split()]

#%%
# n, k = 3, 2
# a = [2, 3, 1]
# b = [1, 3, 2]


#%%
 
dif = {key: dif[key] for key in sorted(dif, key=dif.get, reverse=True)[:k]}


#%%
ans = 0
for i in range(n):
    print(a[i], b[i])
    if i in dif.values():
        ans += b[i]
    else:
        ans += a[i]
print(ans)        
#%%
dif


#%%
