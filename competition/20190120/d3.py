n, k = map(int, input().split())

td = []
for i in range(n):
    t, d = map(int, input().split())
    td.append([t, d])

print(td)

# #%%
# n, k = 5, 3
# td = [[5, 1000000000], [2, 990000000], [3, 980000000],
#       [6, 970000000], [6, 960000000], [4, 950000000]]


#%%
xs = sorted(td, key=lambda x: -x[1])
#%%
print(xs)

#%%
baset = 0
ts = set([])
ds = []



#%%
for t, d in xs[:k]:
    baset += d
    if not t in ts:
        ts.add(t)
    else:
        ds.append(d)




#%%
result = baset + len(ts)**2
r = result

#%%
print(r, ts, ds)

#%%
for t, d in xs[k:]:
    if not ds:
        break
    if not t in ts:
        r += 2 * len(ts) + 1
        r += d - ds.pop()
        ts.add(t)
        result = max(result, r)
        print(r, ts, ds)


#%%
