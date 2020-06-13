# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()

x = 0
while True:
    ans = int(x * 1.08)
    if ans == N:
        print(x)
        break
    elif ans > N:
        print(":(")
        break
    x += 1