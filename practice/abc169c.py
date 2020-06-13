def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

L = input().split()
A = int(L[0])
B = int(L[1].replace(".", ""))


print(int(A*B)//100)