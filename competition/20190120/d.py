n, k = map(int, input().split())

t, d = [], []
for i in range(n):
    ti, di = map(int, input().split())
    t.append(ti)
    d.append(di)

#%%
# n, k = 5, 3
# t = [1, 1, 2, 2, 3]
# d = [9, 7, 6, 5, 1]


#%%
import itertools

#%%
ans = 0
for comb in list(itertools.combinations(range(n), k)):
    delicious = 0
    kinds = []
    kinds_point = 0

    for c in comb:
        delicious += d[c]
        if t[c] not in kinds:
            kinds.append(t[c])
            kinds_point +=1
    kinds_point = kinds_point**2

    satisfaction = delicious + kinds_point
    if satisfaction > ans:
        ans = satisfaction
print(ans)        

#%%
