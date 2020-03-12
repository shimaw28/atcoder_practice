# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
# 全探索(答え候補から)

N = int(input())
S = input()
ans = 0

for i in range(0, 1000):
    i = str(i).zfill(3)
    idx = 0
    for j in range(3):
        if i[j] in S[idx:]:
            idx += S[idx:].index(i[j])+1
            continue
        else:
            break
    else:
        ans += 1

    


print(ans)