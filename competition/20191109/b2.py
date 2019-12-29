N = int(input())
d = [int(i) for i in input().split()]

initial = d[0]
maximum = max(d)

l = [0] * (maximum+1)
l[initial] += 1
for i in range(1, N):
    # if d[i] <= initial:
    #     print(0)
    #     exit()
    l[d[i]] += 1

ans = 1
for i in range(1, maximum):
    if l[i] == 0:
        print(0)
        exit()

    ans *= l[i] ** l[i+1]

print(ans)