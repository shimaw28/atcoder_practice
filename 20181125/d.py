s = input()

#%%
# s = "codethanksfes"

#%%
a = s[0]
ans = 0
for l in s:
    if l<=a:
        a = l
        ans += 1
print(ans)        
#%%
