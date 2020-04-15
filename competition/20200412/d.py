def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N = INT()
S = input()

ans = 0

count_S = {
    "R": [0] * N,
    "G": [0] * N,
    "B": [0] * N,
}ß

count_S[S[-1]][-1] = 1
for i in reversed(range(N-1)):
    count_S["R"][i] = count_S["R"][i+1]
    count_S["B"][i] = count_S["B"][i+1]
    count_S["G"][i] = count_S["G"][i+1]
    count_S[S[i]][i] += 1


# for i in range(0, N-2):
#     for k in range(i+2, N):
#         if S[i]==S[k]:
#             continue
#         for j in range(i+1, k):
#             # print(S[i], S[j], S[k])
#             if j-i!=k-j and S[i]!=S[j] and S[j]!=S[k]:
#                 ans += 1


for i in range(0, N-3):
    for j in range(i+1, N-1):
        if S[i] == S[j]:
            continue
        for c in "RGB":
            if S[i] != c and S[j] != c:
                last_color = c
        ans += count_S[last_color][j+1]
        if j+j-i <= N-1 and S[j+j-i] == last_color:
            ans -= 1

print(ans)