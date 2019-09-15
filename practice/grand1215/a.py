word = input()


#%%
# word = "BWBWBW"


#%%
word.count("W")
#%%
ans = 0
to_plus = word.count("W")
for i in range(len(word)):
    if word[i] == "B":
        ans += to_plus
    else:
        to_plus -= 1

    
print(ans)

