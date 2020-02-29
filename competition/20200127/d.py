import math
H = int(input())

if H == 1:
    print(1)
    exit()



n = int(math.log2(H))
#print(n)
print(2**(n+1)-1)