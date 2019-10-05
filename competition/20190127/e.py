n, m = map(int, input().split())
x = [int(xi) for xi in input().split()]
aby = []
for i in range(m):
    aby.append(list(map(int, input().split())))

# print(n, m, x, aby)


#%%
# n, m = 4, 4
# x = [2, 3, 5, 7]
# aby = [
#     [1, 2, 7,],
#     [1 ,3, 9],
#     [2 ,3, 12],
#     [3 ,4, 18]]


#%%
def sum_up_nodes(x, aby):
    node_set = set()
    for i in aby:
        node_set.add((i[0]))
        node_set.add((i[1]))

    n_sum = 0
    for i in node_set:
        n_sum += x[i-1]
    return n_sum



#%%
ans = 0
loop_flag = True

while loop_flag == True:
    loop_flag = False
    node_sum = sum_up_nodes(x, aby)
    for i in range(len(aby)):
        if aby[i][2] > node_sum:
            aby.pop(i)
            ans += 1
            loop_flag = True
            break

    


#%%
print(ans)


#%%
