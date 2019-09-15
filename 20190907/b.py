n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]


# print(n, a, b, c)

ans = 0
last_index = -1
for ai in a:
    ans += b[ai-1]
    if ai - last_index == 1:
        ans += c[ai-2]
    last_index = ai

print(ans)

