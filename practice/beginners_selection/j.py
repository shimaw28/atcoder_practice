S = input()

#%%
S = "erasedream"
#%%

def check(string):
    if string[0:7] == "dreamer":
        return [string[7:], string[5:]]
    elif string[0:5] == "dream":
        return [string[5:]]
    elif string[0:6] == "eraser":
        return [string[6:], string[5:]]
    elif string[0:5] == "erase":
        return [string[5:]]
    else:
        return "Fail"
    
#%%

s = check(S)

#%%
for i in s:
    print(i)

#%%
