n, h, w = map(int, input().split())

a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

#%%
# n, h, w = [3, 5, 2]

# a = [10, 5, 2]
# b = [3, 2, 5]


#%%
ans = 0
for i in range(n):
    
    # print(a[i], h, b[i], w)
    if a[i] >= h:
        if b[i] >= w:
            ans += 1
print(ans)
#%%
w
