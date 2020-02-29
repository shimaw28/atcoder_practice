import sys
N = int(input())
A = [int(i) for i in input().split()]

a = []
for ai in A:
    if ai in a:
        print("NO")
        Flag = False
    a.append(ai)

if Flag:
    print("YES")