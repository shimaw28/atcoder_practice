def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


A, B, C, D = MAP()


while True:
    C -= B
    if C <= 0:
        print("Yes")
        break
    A -= D
    if A <= 0:
        print("No")
        break
