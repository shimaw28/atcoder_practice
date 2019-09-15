n, T = map(int, input().split())
c, t = [], []

for i in range(n):
    a, b = map(int, input().split())
    c.append(a)
    t.append(b)
#%%
# n, T = 3, 70
# c = list([0,0,0])
# t = list([0,0,0])
# c[0], t[0] =  7, 60
# c[1], t[1] = 1, 80
# c[2], t[2] = 4, 50


#%%
costs = []
min_time  = T
for i in range(n):
    if t[i] <= T:
        costs.append(c[i])

if costs == []:
    print("TLE")
else:
    print(min(costs))    

#%%


#%%
