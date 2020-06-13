def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

T = input()

n = len(T)

ans = []
for i in range(n):
    if T[i] == "?":
        ans.append("D")
    else:
        ans.append(T[i])

print("".join(ans))