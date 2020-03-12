n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

# %%
n = 6
a = [1,     5,    2,     3,     4,     6]

#%%

memo = dict()
ans_list = a[:2]
a = a[2:]

def is_sorted(alist):
    for i in range(len(alist-1)):
        if alist[i] > alist[i+1]:
            return False
    return True


def depth(ans_list, a, move):
    global memo

    if len(a) == 0:
        return ans_list, 0, move
    
    if ans_list[-1] < a[0]:
        ans_list.append(a)
        a = a[1:]
        return ans_list, 0, move
    else:
        for i in ans_list:
            if 



