#%%
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day_to_id = {k: v for v, k in enumerate(days)}
s_list = []



#%%
n = int(input())


#%%
for i in range(n):
    s_list.append(input()) 

#%%
for day in s_list:
    id = day_to_id[day] + 1
    if id == 7:
        id = 0

    print(days[id])
#%%
day_to_id

#%%
