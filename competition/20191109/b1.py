import collections

N = int(input())
d = [int(i) for i in input().split()]

initial = d[0]
maximum = max(d)
d = collections.Counter(d)

ans=1
for n in range(initial, maximum):
    if d[n] == 0:
        print(0)
        exit()
    else:
        ans *= d[n] ** d[n+1]
print(ans)