a, b, k = map(int, input().split())

common = []

for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        common.append(i)


print(common[-k])
