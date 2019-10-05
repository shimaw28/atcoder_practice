n, m = map(int, input().split())
ab = []
prod = [0]
prod_cum = [0]

num_cum = [0]
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a,b])


#%%
ab.sort()

for i in range(n):
    a, b = ab[i][0],ab[i][1]
    # prod.append(a*b)
    prod_cum.append(a*b + prod_cum[-1])
    num_cum.append(b + num_cum[-1])
ab = [[0,0]] + ab
# print(ab)
# print(prod)
# print(prod_cum)
# print(num_cum)
# print(n, m, ab)
# n, m, ab = 4, 30, [[6, 18], [2, 5], [3, 10], [7, 9]]


#%%
ans = 0
prod = 0
for i in range(0, n+1):
    if num_cum[i] >= m:
        print(prod_cum[i] - ab[i][0] * (num_cum[i]-m))
        break



#%%
# ans = 0
# num = 0
# while num < m:
#     a0 = ab[0][0]
#     b0 = ab[0][1]
#     if b0 >= m - num:
#         ans += a0 * (m - num)
#         break
#     else:
#         ans += a0 * b0
#         num += b0
#         ab.remove([a0, b0])
#%%
# print(ans)
#%%
