S = input()

weeklist = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

ans = 7
for w in weeklist:
    if w == S:
        break
    ans -= 1
print(ans)