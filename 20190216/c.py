n = int(input())
a = [int(i) for i in input().split()]

#%%
# n, a = 4, [2, 10, 8, 40]


#%%

def check_end(a):
    if a[0] == 1:
        return 1
    if len(a) == 2:
        if a[1] % a[0] == 0:
            return a[0]
        else:
            return a[1] % a[0]

a.sort()
def attack(a):
    i = 1
    while i < len(a):
        a[i] %= a[0]
        if a[i] <= 0:
            a.remove(a[i])
            if len(a) == 2:
                if a[0] > a[1]:
                    a[0], a[1] = a[1], a[0]
                if a[1] % a[0] == 0:
                    return a[0]
                else:
                    return a[1] % a[0]
            continue
        i += 1
    
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    
    return(attack(a))

print(attack(a))

#%%
