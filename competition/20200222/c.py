N = int(input())
X = [int(i) for i in input().split()]

x_max = max(X)
x_min = min(X)
x_mid = (x_max + x_min)//2

def get_dist(X, a):
    ans = 0
    for xi in X:
        ans += (xi - a)**2
    return ans


direction = 1 #1 => right, -1 => left

x = x_mid
dist1 = get_dist(X, x)
dist2 = get_dist(X, x + 1)

if dist1 > dist2:
    direction = 1
else:
    direction = -1


ans = 0
while True:
    dist2 = get_dist(X, x + direction)

    if dist1 <= dist2:
        ans = dist1
        break

    dist1 = dist2
    x = x + direction
print(ans)

