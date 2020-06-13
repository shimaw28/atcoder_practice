def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()

m = [-1] * (n+1)
m[0] = 1
m[1] = 1

def fib(n):
    if m[n] != -1:
        return m[n]
    
    ans = fib(n-1) + fib(n-2)
    m[n] = ans
    return ans

print(fib(n))
    
