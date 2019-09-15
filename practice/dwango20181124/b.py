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

for ki in k:
    ans = 0
    for a in range(n):
        if "D" == s[a]:
            for b in range(a, min(n, a+ki)):
                if "M" == s[b]:
                    for c in range(b, min(n, a+ki)):                    
                        if "C" == s[c]:
                            ans += 1

    print(ans)





#%%
