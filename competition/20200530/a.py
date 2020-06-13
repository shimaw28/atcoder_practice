def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


H1, M1, H2, M2, K = MAP()
print(max(0, (H2*60+M2) -(H1*60+M1) - K))