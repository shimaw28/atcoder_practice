# 約数全探索
# https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ans = 0
for i in range(1, N+1, 2):
    if len(make_divisors(i)) == 8:
        ans += 1
print(ans)