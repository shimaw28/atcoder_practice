def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


X = INT()

def f(a, b):
    return a**4 + a**3*b + a**2*b**2 + a*b**3 + b**4

for alpha in range(1, int(X**0.5)+1):
    if X % alpha == 0:
        beta = X // alpha

        a = alpha // 2
        b = a - alpha

        while f(a, b) <= beta:
            if f(a, b) == beta:
                break
            a += 1
            b += 1
        
        else:
            continue
        break

print(a, b)