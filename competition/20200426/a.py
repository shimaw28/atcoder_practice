def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

S, W = MAP()

if W >= S:
    print("unsafe")
else:
    print("safe")