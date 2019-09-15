n, q = map(int, input().split())
s = input()
td = []
for _ in range(q):
    t_, d_ = input().split()
    td.append([t_,d_])

#%%
gol = [1] * n

for tdi in td:
    ti = tdi[0]
    di = tdi[1]
    for j, sj in enumerate(s):
        if ti == sj:
            if di == "L":
                if j == 0:
                    gol[j] = 0
                else:
                    gol[j-1] += gol[j]
                    gol[j] = 0
            elif di == "R":
                if j == n-1:
                    gol[n-1] = 0
                else:
                    gol[j+1] += gol[j]
                    gol[j] = 0
    print(gol, sum(gol))

print(sum(gol))
