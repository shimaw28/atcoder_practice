s = input()

flag = "Yes"
for i, step in enumerate(s):
    if i % 2 == 0:
        if step in "RUD":
            pass
        else:
            flag = "No"
            break
    else:
        if step in "LUD":
            pass
        else:
            flag = "No"

print(flag)