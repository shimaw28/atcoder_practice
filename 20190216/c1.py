n = int(input())
a = [int(i) for i in input().split()]


#%%
# n, a = 4, [2, 10, 8, 40]


#%%


#%%

#%%
a.sort()
while len(a) >= 2:
    for i in range(1, len(a)):
        a[i] = a[i] % a[0]
        if a[i] == 1:
            a = [1]
            break
        elif a[i] < a[0] and a[i] != 0:
            a[0], a[i] = a[i], a[0]
            break

        for i in range(len(a)-1, 0):
            if a[i] == 0:
                a.remove(a[i])


#%%
print(a[0])

#%%
