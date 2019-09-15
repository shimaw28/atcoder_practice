s = int(input())


#%%
#s = 8
#%%
def f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3 * n + 1



#%%
a = [s]
ai = 0


#%%
while True:
    # print(a)
    ai = f(a[-1])
    a.append(ai)
    if a.count(ai) == 2:
        break

#%%
print(len(a))

#%%
