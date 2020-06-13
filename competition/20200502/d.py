def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

A, B, N = MAP()

left, right = 0, N

def f(x):
    return int(A*x/B) - A*int(x/B)


# while right-left > 1:
#     mid1 = (left + right)*1// 3
#     mid2 = (left + right)*2// 3

#     if f(mid1) < f(mid2):
#         if left == mid1:
#             break
#         left = mid1
#     else:
#         if right == mid1:
#             break
#         right = mid2

# ans = f(left)
# for i in range(left, right+1):
#     ans = max(ans, f(i))
# print(ans)
# ans = 0
# # whilefor i in range(1, N+1):
# #     ans = max(ans, f(i))
# # print(ans)

# x = N//2
# if f(x) <= f(x)
# direc = "R"

ans = 0
if B > N:
    ans = f(N)
else:
    ans = f(B-1)

print(ans)