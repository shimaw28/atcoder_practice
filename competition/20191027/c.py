N = int(input())

ans = N-1

def get_steps(a, b):
    return (a-1) + (b-1)


for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        d = N // i
        ans = min(ans, get_steps(i, d))

print(ans)