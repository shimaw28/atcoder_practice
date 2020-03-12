# https://atcoder.jp/contests/abc002/tasks/abc002_4

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, M = MAP()
xy = []
for _ in range(M):
    xy.append(tuple(MAP()))

xys = set(xy)

ans = 1
for bits in range(1<<N):
    bits_str = bin(bits)[2:].zfill(N)
    if bits_str.count("1") < 2:
        continue

    party = []
    for i in range(N):
        if bits_str[i] != "1":
            continue

        if len(party) == 0:
            party.append(i)
            continue
        
        for p in party:
            if (p+1, i+1) not in xys:
                break
        else:
            party.append(i) 
            continue
        break
    else:
        ans = max(ans, bits_str.count("1"))
    
    

print(ans)                

    