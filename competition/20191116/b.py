N = int(input())
S = input()

if N % 2 != 0:
    print("No")
    exit()

half_n = N//2

for i in range(half_n):
    if S[i] != S[i+half_n]:
        print("No")
        exit()

print("Yes")
