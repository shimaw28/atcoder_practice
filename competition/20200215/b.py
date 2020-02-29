N = int(input())
A = [int(i) for i in input().split()]

def answer():
    for ai in A:
        if ai % 2 == 0:
            if ai %3 != 0 and ai % 5 != 0:
                return "DENIED"
    
    return "APPROVED"

print(answer())