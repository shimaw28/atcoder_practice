x, y = map(int, input().split())

#%%


#%%
if (x + y) % 4 != 0:
    print("No")
    exit()

#%%
# x = 10
# y = 5

#%%
a = x // 3
b = x % 3
#%%

for n in range(a+1): 
    if 8*n +a + 3*b == y:
        print("Yes")
        exit()
    elif 8*n + a + 3*b > y:
        print("No")
        exit()
        

#%%
