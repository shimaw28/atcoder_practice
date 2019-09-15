n = int(input())
a = input()
b = input()
c = input()

#%%
# n = 4
# a = "west"
# b = "east"
# c = "wait"


#%%
(a[0] == b[0]) + (a[0]==c[0]) + (b[0]==c[0])

#%%
ans = 0
for i in range(n):
    if (a[i] == b[i]) + (a[i] == c[i]) + (b[i] == c[i]) == 1:
        ans+=1
    if (a[i] == b[i]) + (a[i] == c[i]) + (b[i] == c[i]) == 3:
        pass
    if (a[i] == b[i]) + (a[i] == c[i]) + (b[i] == c[i]) == 0:
        ans+=2
print(ans)



#%%
