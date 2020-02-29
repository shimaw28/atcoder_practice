H, N = map(int, input().split())
A = [int(i) for i in input().split()]

# print(sum(A))

if H > sum(A):
    print("No")
else:
    print("Yes")