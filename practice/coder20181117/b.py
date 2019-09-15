inputs = list(input())
gx, gy = map(int, input().split())

# print("inputs are:", inputs, [gx,gy] )

#%%
# inputs = list("WWYWYWWW")
# gx, gy = 3, 0


#%%
#UDLR
import itertools


#%%
inputs_list = ["W", "X", "Y", "Z"]
movements_list = ["U", "D", "L", "R"]


#%%
movements_pattern = list(itertools.permutations(movements_list))

#%% convert
flag = False
for movements in movements_pattern:
    converter = {k: v for k, v in zip(inputs_list, movements)}
    #print(converter)

    moves = [converter[x] for x in inputs]

    position = [0, 0]
    #print("start:", position)
    for m in moves:
        if m == "U":
            position[1] += 1
        elif m == "D":
            position[1] -= 1
        elif m == "L":
            position[0] -= 1
        elif m == "R":
            position[0] += 1

    
        if position == [gx, gy]:
            print("Yes")
            flag = True
            break

    if flag:
        break

if flag != True:
    print("No")

#%%
