n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))


a.sort(reverse=True)

ans = 0
a0 = 0
for i, ai in enumerate(a):
    a0 += ai
    if a0 >= sum(a[i+1:]):
        break
    
    ans += 2**(n-i-1) -2

print(ans*3)