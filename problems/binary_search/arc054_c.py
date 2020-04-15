#https://atcoder.jp/contests/arc054/tasks/arc054_b
#三分探索方

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import math

P = float(input())

def f(x):
    return math.log(x + (P * 2**(-x/1.5)))

left, right = 0, P
while right - left > 10**-10:
    mid1 = left + (right - left)/3
    mid2 = right - (right - left)/3

    if f(mid1) < f(mid2):
        right = mid2
    else:
        left = mid1


print(math.exp(f(left)))
