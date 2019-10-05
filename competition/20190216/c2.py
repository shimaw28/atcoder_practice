n = int(input())
a = [int(i) for i in input().split()]


def euclid_lcf(a, b):
    if b < a:
        a, b = b, a

    if b % a == 0:
        return a
    else:
        r = b % a
        return euclid_lcf(a, r)


com_factor = euclid_lcf(a[0], a[1])

if len(a) == 2:
    print(com_factor)
else:
    for i in range(2, len(a)):
        com_factor = euclid_lcf(com_factor, a[i])

    print(com_factor)
