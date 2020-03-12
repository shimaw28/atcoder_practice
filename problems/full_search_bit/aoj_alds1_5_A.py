# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja

n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
M = [int(i) for i in input().split()]

A.sort()
 
def solve(idx, current_sum, mi):
    if current_sum == mi:
        return True
    elif current_sum > mi:
        return False

    if idx == n-1:
        if current_sum + A[idx] == mi:
            return True
        else:
            return False

    if solve(idx+1, current_sum+A[idx], mi):
        return True
    elif solve(idx+1, current_sum, mi):
        return True
    else:
        return False


for mi in M:
    if solve(0, 0, mi):
        print("yes")
    else:
        print("no")

