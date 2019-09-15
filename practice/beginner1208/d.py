n, x = map(int, input())



#%%
if x <= n:
    print(0)
    exit()
#%%
def num_layer(layer):
    return 8 * 2 ** (layer-1) -3


#%%
def num_buns(layer):
    return 4 * 2 ** (layer-1) -1

#%%

l1 = [0, 1, 2, 3, 3]
#%%
n_layer = num_layer(n)
n_layer

#%%

#%%
n, x = 3, 17
ans = 0
for i in range(n, 1, -1):
    print(ans, i, num_layer(i), x)
    if x > num_layer(i)/2:
        print(True)
        ans += num_buns(i-1) + 1
        x -= num_layer(i-1)/2 + 0.5
    else:
        x -= num_layer(i-1)-0.5
        print(False)
#%%
x

#%%


#%%
