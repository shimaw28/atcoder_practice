n = int(input())
xy = []
for _ in range(n-1):
    xy.append(list(map(int,input().split())))
q = int(input())
ab = []
for _ in range(q):
    ab.append(list(map(int, input().split())))

#print(n, xy, q, ab)

#%%
# n, xy, q, ab = 5, [[1, 2], [1, 3], [1, 4], [4, 5]], 3, [[2, 3], [2, 5], [2, 4]]


#%%

start = ab[0][0]
end = ab[0][1]

#%%
def check_torus(start, end, nodes, step, flag=False):
    if flag:
        return True, step
    if start == end:
        return True, step + 1
    for node in nodes:
        if flag:
            continue
        if start == node[0]:
            # print("found!", start, end, node[1])
            new_nodes = nodes[:]
            new_nodes.remove(node)
            flag, step = check_torus(node[1], end, new_nodes, step+1, flag)
        elif start == node[1]:
            # print("found!", start, end, node[0])
            new_nodes = nodes[:]
            new_nodes.remove(node)
            flag, step = check_torus(node[0], end, new_nodes, step+1, flag)

    if flag:
        return True, step
    else:
        return False, step - 1

#%%
step = 0
for abi in ab:
    print(check_torus(abi[0], abi[1], xy, step)[1])

#%%
