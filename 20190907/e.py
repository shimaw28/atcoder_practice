n = int(input())
p = [int(i) for i in input().split()]

ans = 0

def check(p, l, r, largest, second, ans):
    m = 0
    for i in range(l):
        check_index = l-i-1
        if p[check_index] > second or p[check_index] > largest:
            continue
        else:
            m += 1

    for i in range(len(p)-r-1):
        check_index = r + i + 1
        if p[check_index] > second or p[check_index] > largest:
            continue
        else:
            m += 1

    return second * m

for i in range(n):
    a = p[i]

    if a == n :
        continue

    largest_flag = True
    largest = a
    second_flag = False
    second = a
    for j in range(i):
        b = p[i-j-1]
        if b > a:
            largest = b
            second = a
            ans += check(p, i-j-1, i, largest, second, ans)
            continue

    for j in range(len(p)-i-1):
        b = p[i+j+1]
        if b > a:
            largest = b
            second = a
            ans += check(p, i, i+j+1, largest, second, ans)
            continue
print(ans)