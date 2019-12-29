N = int(input())
S = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = []
for s in S:
    for i, a in enumerate(alphabet):
        if s == a:
            break
    ans.append(alphabet[(i + N) % 26])

print("".join(ans))