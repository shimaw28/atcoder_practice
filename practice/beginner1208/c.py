n, k = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))

#%%
# n, k = 5, 3
# h = [10, 15, 11, 14, 12]


#%%
h.sort()

#%%

#%%
picked = h[:k]


#%%
ans = h[k-1] -h[0]


#%%
dif = ans

for i in range(n - k):
    dif += h[i] - h[i+1]
    dif += h[i + k] - h[i + k - 1]
    if ans > dif:
        ans = dif
    # print(dif)

#%%
print(ans)

#%%
