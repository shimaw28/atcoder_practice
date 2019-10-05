n = int(input())
h = [int(hi) for hi in input().split()]


#%%

#add 0 for both sides


#%%
#singlify 0
def singlify(h):
    # print(h)
    h = [0] + h + [0]
    # print(h)
    newh = []
    zero_flag = False
    for i in range(len(h)):
        if h[i] == 0:
            zero_flag = True
        else:
            if zero_flag:
                newh.append(0)
            newh.append(h[i])
            zero_flag = False
        # print(newh)
    newh.append(0)
    return newh


#%%
def minus_one_and_not_lower_than_zero(h):
    for i in range(len(h)):
        h[i] -= 1
        if h[i] == -1:
            h[i] = 0
    return h
#%%
# h = [3,1,2,3,1]

#%%
ans = 0

while True:
    h = singlify(h)
    # print(h)
    ans += h.count(0)-1
    h = minus_one_and_not_lower_than_zero(h)

    if sum(h) == 0:
        break

print(ans)
#%%


#%%
