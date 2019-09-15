n, q = map(int, input().split())
s = input()
td = []
for _ in range(q):
    t_, d_ = input().split()
    td.append([t_,d_])

#%%

#n, q, s, td = 10, 15, "SNCZWRCEWB", [['B', 'R'], ['R', 'R'], ['E', 'R'], ['W', 'R'], ['Z', 'L'], ['S', 'R'], ['Q', 'L'], ['W', 'L'], ['B', 'R'], ['C', 'L'], ['A', 'L'], ['N', 'L'], ['E', 'R'], ['Z', 'L'], ['S', 'L']]


td = [["W", "L"], ["R", "L"], ["C", "L"], ["E", "L"]] + td
#%%
ans = 0
left_target_idx = 0
right_target_idx = -1
for tdi in td[::-1]:
    ti = tdi[0]
    di = tdi[1]

    print(tdi)
    if left_target_idx > n-1 or right_target_idx < -n:
        break

    if di == "L":
        if ti == s[left_target_idx]:
            ans += 1
            left_target_idx += 1
            print("L")
    elif di == "R":
        if ti == s[right_target_idx]:
            ans += 1
            right_target_idx -= 1
            print("R")

print(max(n-ans,0))

#%%
