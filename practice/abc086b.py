# https://atcoder.jp/contests/abc086/tasks/abc086_b

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

a, b = input().split()

i = int(a+b)

if (i ** 0.5) % 1 == 0:
    print("Yes")
else:
    print("No")

    