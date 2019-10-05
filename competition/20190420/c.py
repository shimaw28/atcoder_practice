n = int(input())
s = input()


def main(s):
    if s.count("#") == 0 or s.count(".") == 0:
        print(0)
        return

    strip_left = s.find("#")
    s = s[strip_left:]

    strip_right = s[::-1].find(".")
    if strip_right != 0:
        s = s[:-strip_right]
    
    n = len(s)
    n_white = s.count(".")

    ans = 0
    for i, l in enumerate(s):
        if i <= n_white-1:
            if l == "#":
                ans += 1
        else:
            if l == ".":
                ans += 1

    print(min(ans, n_white, n-n_white))
    return
#%%
main(s)



#%%


#%%


#%%

