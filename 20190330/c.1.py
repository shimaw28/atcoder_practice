n, q = map(int, input().split())
s = input()
td = []
for _ in range(q):
    t_, d_ = input().split()
    td.append([t_,d_])

#%%
gol = [1] * n

dict_s = {}
for i, si in enumerate(s):
    if si in dict_s:
        dict_s[si].append(i)
    else:
        dict_s[si] = [i]


for tdi in td:
    ti = tdi[0]
    di = tdi[1]

    if ti not in s:
        continue

    for idx in dict_s[ti]:
        if di == "L":
            if idx == 0:
                gol[idx] = 0
            else:
                gol[idx-1] += gol[idx]
                gol[idx] = 0
        elif di == "R":
            if idx == n-1:
                gol[n-1] = 0
            else:
                gol[idx+1] += gol[idx]
                gol[idx] = 0

print(sum(gol))
