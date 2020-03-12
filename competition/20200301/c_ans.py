import sys
N, M = map(int, input().split())
sc = [list(map(int, input().split())) for i in range(M)]

for i in range(10**N):
    if len(str(i)) < N:
        continue
    lst = list(str(i))
    for s, c in sc:
        if int(lst[s-1])==c:
            continue
        else:
            break
    else:
        print(i)
        exit()
print(-1)