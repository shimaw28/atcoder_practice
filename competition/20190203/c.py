n, m = map(int, input().split())
x = list(map(int, input().split()))

# print(n, m, x)

#%%
n, m =2, 5
x = [10, 12, 1, 2, 14]


#%%
x.sort()

#%%




#%%

diff_list = []
for i in range(m-1):
    diff = x[i+1] - x[i]
    diff_list.append(diff)


#%%
diff_list.sort()


#%%
if n-1>0:
    print(sum(diff_list[:-(n-1)]))
else:
    print(sum(diff_list))    

#%%


#%%
