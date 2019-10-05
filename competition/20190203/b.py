n = int(input())
l = list(map(int, input().split()))


#%%
# n = 4
# l = [3, 8, 5, 1]



#%%
l.sort()

if l[-1] < sum(l[:-1]):
    print("Yes")
else:    
    print("No")

#%%
