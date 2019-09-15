n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])


#%%
# n, m, ab = 4, 5, [[1, 2], [3, 4], [1, 3], [2, 3], [1, 4]]


#%%
import math

#%%
n_comb = math.factorial(n) // (math.factorial(n-2) * math.factorial(2))



#%%
ans_list = [n_comb]


#%%
group_sets = [group(ab[-1])]

for abi in ab[::-1]:
    ai, bi = abi

    difficulty = 0
    flag_new = True

    i = 0
    while i <= len(group_sets):
        g = group_sets[i]
        if ai in g:
            flag_double = False
            for g2 in group_sets[i+1:]:
                if bi in g2:
                    difficulty += (len(g) + len(g2))
                    for g2i in g2:
                        g.add(g2i)
                    group_sets.remove(g2)
                    flag_double = True
                    continue
            if flag_double:
                flag_new = False
                continue
            else:
                difficulty += len(g)
                g.add(bi)
                flag_new = False
        elif bi in g:
            flag_double = False
            for g2 in group_sets[i+1:]:
                if ai in g2:
                    difficulty += (len(g) + len(g2))
                    for g2i in g2:
                        g.add(g2i)
                    group_sets.remove(g2)
                    flag_double = True
                    continue
            if flag_double:
                flag_new = False
                continue
            else:
                difficulty += len(g)
                g.add(bi)
                flag_new = False

    if flag_new:
        group_sets.append({ai, bi})
        difficulty += 1
    
    ans_list.append(max(ans_list[-1] - difficulty, 0))


#%%
ans_list = ans_list[:-1]
for i in ans_list[::-1]:
    print(i)

#%%


#%%
