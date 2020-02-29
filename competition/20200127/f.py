N, D, A = map(int, input().split())
XH = []
for _ in range(N):
    XH.append(list(map(int, input().split())))

XH.sort(key=lambda x:x[0])

ans=0
for i in range(len(XH)):
    if XH[i][1] <= 0:
        continue

    while XH[i][1] > 0:
        r = 2*D + 1   
        XH[i][1] -= A
        ans += 1
        for j in range(i+1, len(XH)):
            if XH[i][0] + r > XH[j][0]:
                XH[j][1] = -A
            else:
                break
        
print(ans)
