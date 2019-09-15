n = int(input())
t, a = map(int,input().split())
result = 0
min_dif = 9999999

for i, x in enumerate(map(int, input().split())):
    if min_dif > abs(a - (t - x * 0.006)):
        result = i+1
        min_dif = abs(a - (t - x * 0.006))

print(result)
