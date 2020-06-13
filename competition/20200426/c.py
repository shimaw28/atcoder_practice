def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


N = INT()
prize = set()

for _ in range(N):
    prize.add(input())

print(len(prize))
