n, y = map(int, input().split())

#%%
break_flag = False
for yukichi in range(n + 1):
    if y < 10_000 * yukichi:
        break

    for higuchi in range(yukichi, n+1):
        if y < 10_000 * yukichi + 5000*higuchi:
            break
        
        noguchi = n - yukichi - higuchi

        if 10_000*yukichi + 5000*higuchi + 1000*noguchi == y:
            print(yukichi, higuchi, noguchi)
            break_flag = True
            break
    
    if break_flag:
        break

if break_flag:
    pass
else:
    print("-1 -1 -1")    