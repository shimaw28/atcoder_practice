alist = []
for _ in range(5):
    alist.append(int(input()))



#%%
ans = 0
for i in alist:
    ans += ((i-1) // 10 + 1) *10
    # print(ans)

ans_b = 11
for i in alist:
    if i % 10 == 0:
        ans_b = min(ans_b, 10)
    else:
        ans_b = min(ans_b, i%10)

print(ans - (10 - ans_b))
#%%
