n = int(input())
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())



#%%
# n = 6
# a = [3, 14, 159, 2, 6, 53]
# b = [58, 9, 79, 323, 84, 6]
# c = [2643, 383, 2, 79, 50, 288]

#%%
a=sorted(a)
b=sorted(b)
c=sorted(c)

#%%
ans = 0

for ci in c:
    for bi in b:
        if ci > bi:
            for ai in a:
                if bi > ai:
                    # print(ci, bi, ai)
                    ans += 1
                else:
                    break
        else:
            break

#%%
print(ans)

#%%
