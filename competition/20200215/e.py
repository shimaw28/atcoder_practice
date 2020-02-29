N = input()

ans = 0

flag = False
for d in list(N):
    d = int(d)

    if d <= 5:
        ans += d
        flag = False
    else:
        if flag:
            ans += -1 + (10 - d) 
        else:
            ans += 1 + (10 - d)
        flag = True        

print(ans)