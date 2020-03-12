S = input()
n = len(S)

length = 0

for s in range(n):
    for e in range(s, n):
        if all("ACGT".count(c)==1 for c in S[s:e+1]):
            length = max(length, e-s+1)

print(length)