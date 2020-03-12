def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, A, B = MAP()



sets = N // (A+B) 
remain = N % (A+B)

blues = sets * A + min(remain, A)
print(blues)