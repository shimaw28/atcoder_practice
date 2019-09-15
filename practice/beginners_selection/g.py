n = int(input())
a = [int(i) for i in input().split()]

a.sort()
a = a[::-1]


alice = a[::2]
bob = a[1::2]
print(sum(alice) - sum(bob))


