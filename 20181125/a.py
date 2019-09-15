t, a, b, c, d = map(int, input().split())

#%%
# t, a, b, c, d = 100,20, 500, 40, 1000


#%%

if t >= a + c:
    print(b+d)
    exit()
elif t >= c:
    print(d)
    exit()
elif t >= a:
    print(b)    
    exit()
else:
    print(0)
    

#%%
