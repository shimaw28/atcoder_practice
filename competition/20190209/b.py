ab = []
for _ in range(3):
    ab.append(list(map(int,input().split())))

#%%
# ab = [
# [4, 2],
# [1, 3],
# [2, 3]]

#%%
node = [0] * 4


#%%


for abi in ab:
    node[abi[0]-1] += 1
    node[abi[1]-1] += 1


#%%
if len(ab) < 3:
    print("NO")
elif 3 in node:
    print("NO")
else:
    print("YES")

#%%
