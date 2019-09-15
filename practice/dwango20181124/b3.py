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
ans = [0 for _ in range(q)]
for a in idx_a:
    for c in idx_c[a::-1]:
        if a<c:
            for w in s[a:c]:
                if w =="M":
                    ans += 1
        break

    print(ans)





#%%
