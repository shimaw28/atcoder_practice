N, A, B = map(int, input().split())


#%%
ans = 0
for i in range(1, N+1):
    sum_digits = sum(list(map(int, list(str(i)))))
    if A <= sum_digits and sum_digits <= B:
        ans += i
print(ans)
#%%
