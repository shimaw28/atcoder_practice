A, B, C = map(int, input().split())

def ans():
    if A == B and B==C:
        return "No"
    elif A == B:
        return "Yes"
    elif C == B:
        return "Yes"
    elif C == A:
        return "Yes"
    else:
        return "No"

print(ans())
