n = int(input())
d = [int(i) for i in input().split()]

initial = d[0]
maximum = max(d)

count_dict = {}
count_dict[initial] = 1

for i in range(1, n):
    if d[i] <= initial:
        print(0)
        exit()

    if d[i] in count_dict.keys():
        count_dict[d[i]] += 1
    else:
        count_dict[d[i]] = 1

count_dict = sorted(count_dict.items())

# print(len(count_dict))

ans = 1
for i in range(len(count_dict)-1):
    if count_dict[i][0] + 1 != count_dict[i+1][0]:
        print(0)
        exit()

    ans *= count_dict[i][1] **count_dict[i+1][1]

print(ans)