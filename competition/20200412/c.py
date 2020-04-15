def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import math
from functools import reduce
from itertools import combinations_with_replacement

def gcd(*numbers):
    return reduce(math.gcd, numbers)
    
K = INT()

# memo = []
# for i in range(K):
#     memo2 = []
#     for j in range(K):
#         memo2.append([-1] * K)
#     memo.append(memo2)


# def memorize(i, j, k, a):
#     memo[i-1][j-1][k-1] = a

ans = 0
lst = list(range(1, K+1))

for a, b, c in combinations_with_replacement(lst, 3):
    if a == b and b == c:
        ans += gcd(a, b, c)
    elif a == b or b == c or c==a:
        ans += gcd(a, b, c) * 3
    else:
        ans += gcd(a, b, c) * 6

print(ans)
