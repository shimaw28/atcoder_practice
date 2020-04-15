def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


a, b, c = MAP()

import math

if 4*a*b < (c-a-b)**2:
    print("Yes")
else:
    print("No")