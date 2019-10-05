n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b, a+b])


#%%
# n = 3
# ab = [
# [20, 10, 30],
# [20, 20, 40],
# [20, 30, 50]]


#%%
ab.sort(key=lambda x: -x[2])


    


#%%
takahashi = 0
for i in ab[0::2]:
    takahashi += i[0]

aoki = 0
for i in ab[1::2]:
    aoki += i[1]

#%%
print(takahashi - aoki)

#%%
