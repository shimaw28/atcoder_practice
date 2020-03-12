# https://atcoder.jp/contests/abc128/tasks/abc128_c

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

ans = 0
for x in product([0, 1], repeat=N):
    for i in range(M):
    	cnt = 0
    	for n in s[i]:
    		if x[n-1] == 1:
    			cnt += 1
    	if cnt%2 != p[i]:
    		break
    else:
    	ans += 1
print(ans)

# def judge_bulbs(switches):
#     for i in range(M):

#         k_sum = 0
#         for ki in range(k[i]):
#             k_sum += switches[ki]

#         if k_sum % 2 == p[i]:
#             continue
#         else:
#             return False
#     return True

# def solve(idx, switches):
#     if idx == N:
#         if judge_bulbs(switches):
#             return 1
#         else:
#             return 0

#     ans = 0
#     switches = switches.copy()
    
#     ans += solve(idx+1, switches)

#     switches[idx] = 1
#     ans += solve(idx+1, switches)
#     return ans

# print(solve(0, switches))

ans = 0

for x in product([0, 1], repeat=N):
    for i in range(M):
        cnt = 0
        for n in s[i]:
            if x[n-1] == 1:
                cnt += 1
        if cnt % 2 != 0:
            break
    else:
        ans += 1
print(ans)
    

