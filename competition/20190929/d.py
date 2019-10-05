a, b = map(int, input().split())
A, B = a, b
ans = 1

n = 2

while n <= int(max(A, B)**0.5)+1:
    if a%n == 0 and b%n == 0:
        while a%n == 0:
            a = a//n
        while b%n == 0:
            b = b//n
        ans += 1
    
    n += 1
print(ans)
