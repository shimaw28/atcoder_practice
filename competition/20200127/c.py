N, K = map(int, input().split())
H = [int(i) for i in input().split()]

H.sort(reverse=True)

if K==0:
    print(sum(H))
elif K >= N:    
    print(0)
else:
    print(sum(H[K:]))