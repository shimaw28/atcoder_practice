

n, m = map(int, input().split())

a = []
k = []
for _ in range(n):
    ka = [int(i) for i in input().split()]
    k.append(ka[0])
    a.append(ka[1:])


# print(n, m, k, a)
#%%
# n,m,k,a = 3, 4, [2, 3, 2], [[1, 3], [1, 2, 3], [3, 2]]

#%%
def main():
    
    food = a[k.index(max(k))]

    for i in range(len(a)):
        for f in food:
            if f in a[i]:
                continue
            else:
                food.remove(f)
        if len(food) == 0:
            return 0
    return len(food)

print(main())    
#%%
# k.index(max(k))


#%%
