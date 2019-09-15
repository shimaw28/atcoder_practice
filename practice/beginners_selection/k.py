n = int(input())
t, x, y = [], [], []
for _ in range(n):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)


#%%
x.insert(0,0)
y.insert(0,0)
t.insert(0,0)

#%%
for i in range(n):
    # print(x[i], y[i], x[i+1], y[i+1], t[i], t[i+1])
    if (abs(x[i]-x[i+1]) + abs(y[i]-y[i+1])) > abs(t[i]-t[i+1]):
        print("No")
        exit()
    elif (abs(x[i]-x[i+1]) + abs(y[i]-y[i+1])) % 2 != (t[i]-t[i+1]) % 2:
        print("No")
        exit()

        
print("Yes")    

#%%
