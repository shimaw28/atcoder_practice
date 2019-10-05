n, m = map(int, input().split())
a = list(map(int, input().split()))


#%%
# n, m, a = 10, 6, [2, 3, 3, 3, 4, 4, 4, 5, 5, 6]


#%%
a.sort()
ans = 0
#%%
def check_triple(a, ans):
    if len(a) < 2:
        return ans

    start = a[0]
    same = 0
    consecutive = 0


    if a[1] == start and a[2] == start:
        same =  check_triple(a[3:], ans + 1)


    if start+1 in a and start+2 in a:
        new_a = a[:]
        new_a.remove(start+1)
        new_a.remove(start+2)
        # for i in range(1, len(a)):
        #     if new_a[i] == start+1:
        #         idx1 = i
        #     elif new_a[i] == start+2:
        #         idx2 = i
        # new_a.pop(idx2)
        # new_a.pop(idx1)
        consecutive = check_triple(new_a[1:], ans + 1)

    return max(ans, same, consecutive)
#%%
print(check_triple(a, ans))
