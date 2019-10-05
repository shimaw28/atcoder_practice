n, m = map(int, input().split())

a = []
k = []
for _ in range(n):
    ka = [int(i) for i in input().split()]
    k.append(ka[0])
    a.append(ka[1:])

#%%

mlist = [0] * m

#%%
for i in range(len(a)):
    for j in range(len(a[i])):
        mlist[a[i][j] - 1] += 1

counter = 0
for mlisti in mlist:
    if mlisti == n:
        counter += 1

print(counter)
#%%
