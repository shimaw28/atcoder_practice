N = int(input())
g = []
for _ in range(N-1):
    a, b = map(int, input().split())
    g.append((a,b))


d = {}
for i in range(1, N+1):
    d[i] = []
d_lines = {}
col = [1]
n_cols = 1

d[g[0][0]].append(1)
d[g[0][1]].append(1)

d_lines[1] = [g[0][0], g[0][1]]

for gi in g[1:]:
    a, b = gi[0], gi[1]

    n = 1
    while True:
        if n not in d[a]:
            break
        else:
            n += 1
    col.append(n)
    n_cols = max(n_cols, n)
    d[a].append(n)
    d[b].append(n)

print(n_cols)
for c in col:
    print(c)

