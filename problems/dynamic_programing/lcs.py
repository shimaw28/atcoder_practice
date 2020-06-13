#longest common sequence

s = input()
t = input()

len_s = len(s)
len_t = len(t)
DP = [[0] * (len_t+1) for _ in range(len_s+1)]

ans = []
ans_len = 0

for i in range(1, len_s+1):
    flag = True
    for j in range(1, len_t+1):
        if s[i-1] == t[j-1] and flag:
            if DP[i-1][j] >= DP[i][j-1]+1:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i][j-1]+1
                flag = False
                ans.append(s[i-1])
                ans_len += 1
        else:
            DP[i][j] = DP[i][j-1]

print("".join(ans))


