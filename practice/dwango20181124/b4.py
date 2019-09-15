n = int(input())
s = input()
q = int(input())
k = [int(i) for i in input().split()]

#%%
# n = 54
# s = "DIALUPWIDEAREANETWORKGAMINGOPERATIONCORPORATIONLIMITED"
# q = 3
# k = [20, 30, 40]


#%%
idx_a = []
idx_b = []
idx_c = []

#%%
for i in range(len(s)):
    if s[i] == "D":
        idx_a.append(i)
    if s[i] == "M":
        idx_b.append(i)
    if s[i] == "C":
        idx_c.append(i)


#%%
import itertools

for ki in k:
    ans=0
    for i in itertools.product(idx_a, idx_b, idx_c):
        if i[2]-i[0]<ki and i[0]<i[1] and i[1]<i[2]:
            ans += 1
    print(ans)

#%%
