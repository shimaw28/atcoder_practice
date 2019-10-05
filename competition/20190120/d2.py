n, k = map(int, input().split())

td = []
for i in range(n):
    t, d = map(int, input().split())
    td.append([t, d])

print(n, k, td)

#%%
n, k = 5, 3
td = [[5, 1000000000], [2, 990000000], [3, 980000000],
      [6, 970000000], [6, 960000000], [4, 950000000]]


#%%
sorted_list = sorted(td, key=lambda x:x[0])


#%%
# new_list = []
# counter = 0
# for i in range(len(sorted_list)-1, 0,-1):
#     # print(i, sorted_list[i][0])
#     if sorted_list[i][0] == sorted_list[i-1][0]:
#         counter += 1
#         if counter <= k:
#             new_list.append(sorted_list[i-1])
#     else:
#         new_list.append(sorted_list[i-1])
#         counter = 0

#%%
picked = sorted_list[:-k]

counter = []
delicious = 0
for i in picked:
    delicious += i[1]
    if i[0] not in counter:
        counter.append(i[0])
satisfaction = delicious + len(counter) ** 2
    

#%%
satisfaction

#%%
