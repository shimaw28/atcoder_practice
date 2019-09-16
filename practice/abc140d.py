n, k = map(int, input().split())
s = input()


#count happy people
def count_happy(s):
    counter=False
    happy = 0
    for si in s:
        if si == "R" and counter:
            happy += 1
        elif si == "R":
            counter=True
        else:
            counter=False
    counter = False
    for si in s[::-1]:
        if si == "L" and counter:
            happy += 1
        elif si == "L":
            counter=True
        else:
            counter=False
    return happy

#group
happy = count_happy(s)

new_s = [s[0]]
last_char = s[0]
for si in s[1:]:
    if si == last_char:
        continue
    else:
        new_s.append(si)
        last_char = si

happy += min(len(new_s)//2, k)*2

if len(new_s)%2 == 0 and len(new_s)//2 <= k:
    happy -= 1

print(happy)
