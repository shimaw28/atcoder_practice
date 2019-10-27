import math

a, b, x = map(int, input().split())

if b*a/2 <= x/a:
    theta = math.degrees(math.atan(2*b/a - 2*x/a**3))

else:
    theta = math.degrees(math.atan(b**2*a/x/2))

print(theta)
