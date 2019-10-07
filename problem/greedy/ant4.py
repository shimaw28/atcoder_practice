#p47 ahsaruman's army
#poj3069

n = 6
r = 10
x = [1,7,15,20,30,50]

i = 0
ans = 0

while i < n:
    s = x[i]
    while i < n and x[i] <= s+r:
        i += 1
    p = x[i-1]
    while i < n and x[i] <= p+r:
        i += 1
    ans += 1

print(ans)
