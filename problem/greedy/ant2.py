#p43 scheduling問題
from collections import deque
n = 5
s = [1,2,4,6,8] #start
t = [3,5,7,9,10] #end

ans = 1

p = [(ti, si) for ti, si in zip(t, s)]
p.sort()
p = deque(p)

curr = p.popleft()
while len(p) > 0:
    if p[0][1] > curr[0]:
        ans += 1
        curr = p.popleft()
    else:
        p.popleft()
    
print(ans)    