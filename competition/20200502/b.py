def INT(): return int(input())
def MAP(): return map(int, input().split())


X = INT()

year = 0
cash = 100
while cash < X:
    year += 1
    cash = int(cash * 1.01)

print(year)