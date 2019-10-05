k, a, b = map(int, input().split())

#%%
#k, a, b = 4, 2, 6


#%%
def main(biscuit, k, a, b):
    if k < a + 1:
        return biscuit + k


    dif = b - a

    if dif > 2:
        if biscuit < a:
            new_biscuit = a
            new_k = k - a
            return main(new_biscuit, new_k, a, b)
        else:
            new_k = k - 2
            new_biscuit = biscuit + dif
            return main(new_biscuit, new_k, a, b)
    else:
        return biscuit + k


print(main(1, k, a, b))

#%%
