n = int(input())
a = [int(i) for i in input().split()]

ans = [0] * n

for i, ai in enumerate(a):
    ans[ai-1] = i+1

print(" ".join([str(s) for s in ans]))