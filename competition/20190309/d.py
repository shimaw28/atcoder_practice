a, b = map(int, input().split())

#%%
# a, b = 123, 456



#%%
def cum_xor(n):
    if n % 2 == 1:
        n_1 = (n+1) // 2
        if n_1 % 2 == 0:
            return 0
        else:
            return 1
    else:
        n_1 = n // 2
        if n_1 % 2 == 0:
            return n
        else:
            return 1 ^ n



#%%
print(cum_xor(a-1) ^ cum_xor(b))

#%%
